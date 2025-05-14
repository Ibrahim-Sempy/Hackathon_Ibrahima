from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Report, Vote, Comment
from .forms import ReportForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.contrib.admin.views.decorators import staff_member_required

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    comments = report.comments.all().order_by('-created_at')
    vote_count = report.votes.count()
    user_has_voted = request.user.is_authenticated and report.votes.filter(user=request.user).exists()

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.report = report
            comment.user = request.user
            comment.save()
            return redirect('report_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'reports/report_detail.html', {
        'report': report,
        'comments': comments,
        'vote_count': vote_count,
        'user_has_voted': user_has_voted,
        'form': form,
    })

def report_delete(request, pk):
    report = Report.objects.get(pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'reports/report_confirm_delete.html', {'report': report})

def report_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_detail', pk=report.pk)
    else:
        form = ReportForm(instance=report)
    return render(request, 'reports/report_edit.html', {'form': form})

def report_map(request):
    reports = Report.objects.exclude(latitude__isnull=True, longitude__isnull=True)
    problem_type = request.GET.get('problem_type')
    status = request.GET.get('status')
    if problem_type:
        reports = reports.filter(problem_type=problem_type)
    if status:
        reports = reports.filter(status=status)
    return render(request, 'reports/report_map.html', {
        'reports': reports,
        'selected_problem_type': problem_type,
        'selected_status': status,
    })

@login_required
def vote_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    Vote.objects.get_or_create(report=report, user=request.user)
    return redirect('report_detail', pk=pk)

@login_required
def report_stats(request):
    total_reports = Report.objects.count()
    reports_by_type = Report.objects.values('problem_type').annotate(count=Count('id'))
    reports_by_status = Report.objects.values('status').annotate(count=Count('id'))
    avg_votes = Vote.objects.values('report').annotate(votes=Count('id')).aggregate(avg=Avg('votes'))['avg'] or 0
    top_reports = Report.objects.annotate(num_votes=Count('votes')).order_by('-num_votes')[:5]
    return render(request, 'reports/report_stats.html', {
        'total_reports': total_reports,
        'reports_by_type': reports_by_type,
        'reports_by_status': reports_by_status,
        'avg_votes': avg_votes,
        'top_reports': top_reports,
    })

@staff_member_required
def admin_report_list(request):
    status = request.GET.get('status', '')
    problem_type = request.GET.get('problem_type', '')
    reports = Report.objects.all()
    if status:
        reports = reports.filter(status=status)
    if problem_type:
        reports = reports.filter(problem_type=problem_type)
    # Statistiques pour le diagramme
    status_stats = reports.values('status').annotate(count=Count('id'))
    status_labels = []
    status_counts = []
    status_map = dict(Report._meta.get_field('status').choices)
    for stat in status_stats:
        status_labels.append(status_map.get(stat['status'], stat['status']))
        status_counts.append(stat['count'])
    return render(request, 'reports/admin_report_list.html', {
        'reports': reports,
        'selected_status': status,
        'selected_problem_type': problem_type,
        'status_labels': status_labels,
        'status_counts': status_counts,
    })

@staff_member_required
def admin_report_status(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Report._meta.get_field('status').choices):
            report.status = new_status
            report.save()
    return redirect('admin_report_list')