from django.shortcuts import redirect, render

def home(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    return render(request, 'home.html')