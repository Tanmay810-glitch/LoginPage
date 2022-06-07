from django.shortcuts import render

# Create your views here.
def lp(request):
    return render(request, "LoginPage/login.html")

def lps(request):
    return render(request, "LoginPage/login_success.html")