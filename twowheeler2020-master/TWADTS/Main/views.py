from django.shortcuts import render

# Create your views here.
def signup(request):
    print('sign up')
    return render(request, 'login_pages/signup.html')
def landing(request):
    return render(request, 'landingpage.html')

def user_dashbord(request):
    return render(request, 'user_dashbord.html')

def feedback(request):
    return render(request, 'feedback/feedback.html')

def faq(request):
    return render(request, 'faq/faq-1.html')

def invoice(request):
    return render(request, 'invoice-2.html')
