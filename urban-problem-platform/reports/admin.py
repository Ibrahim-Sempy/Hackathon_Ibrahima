from django.contrib import admin
from .models import Report, Vote, Comment
import csv
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'problem_type', 'status', 'created_at', 'user')
    list_filter = ('status', 'problem_type', 'created_at')
    search_fields = ('description',)
    actions = ['export_as_csv', 'mark_in_progress', 'mark_resolved']

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Exporter la sélection en CSV"

    def mark_in_progress(self, request, queryset):
        updated = queryset.update(status='in_progress')
        for report in queryset:
            if report.user and report.user.email:
                send_mail(
                    'Votre signalement est en cours de traitement',
                    f'Bonjour {report.user.username},\n\nVotre signalement "{report.description[:50]}" est maintenant en cours de traitement.',
                    settings.DEFAULT_FROM_EMAIL,
                    [report.user.email],
                    fail_silently=True,
                )
    mark_in_progress.short_description = "Marquer comme En cours"

    def mark_resolved(self, request, queryset):
        updated = queryset.update(status='resolved')
        for report in queryset:
            if report.user and report.user.email:
                send_mail(
                    'Votre signalement a été résolu',
                    f'Bonjour {report.user.username},\n\nVotre signalement "{report.description[:50]}" a été marqué comme résolu. Merci pour votre contribution !',
                    settings.DEFAULT_FROM_EMAIL,
                    [report.user.email],
                    fail_silently=True,
                )
    mark_resolved.short_description = "Marquer comme Résolu"

admin.site.register(Vote)
admin.site.register(Comment)