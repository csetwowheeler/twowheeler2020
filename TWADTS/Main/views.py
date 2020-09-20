from django.shortcuts import render
from django.shortcuts import get_object_or_404

from Users.models import SignUp
from Main.models import Feedback

# Create your views here.


def signup(request):
    print('sign up')
    return render(request, 'login_pages/signup.html')


def landing(request):
    return render(request, 'landingpage.html')


def user_dashbord(request):
    return render(request, 'user_dashbord.html')


def contact_us(request):
    return render(request, 'live_tracking/maps.html')


def feedback(request):

    if request.method == 'GET':
        try:
            email = request.session['username']
            user = get_object_or_404(SignUp, Email=email)
            feedback = get_object_or_404(Feedback, user=user)
            rating = feedback.rating
            return render(request, 'feedback/feedback.html', {'feedback': feedback, 'rating': rating})
        except Exception:
            print('2')
            return render(request, 'feedback/feedback.html', {'no_records': 'no_records'})
    if request.method == 'POST':
        try:
            email = request.session['username']
            user = get_object_or_404(SignUp, Email=email)
            rating = int(request.POST['rating'])
            feedback = request.POST['feedback']
            suggestion = request.POST['suggestion']
            issue = request.POST['issue']

            try:
                fb = Feedback.objects.get(user=user)
                fb.rating = rating
                fb.feedback = feedback
                fb.suggestion = suggestion
                fb.issue = issue
                fb.save()
                return render(request, 'feedback/feedback.html', {'rating': rating})
            except:
                fb = Feedback.objects.create(
                    user=user, rating=rating, feedback=feedback, suggestion=suggestion, issue=issue)
                fb.save()
            return render(request, 'feedback/feedback.html', {'rating': rating})
        except Exception as e:
            print('3')
            print(e)
            return render(request, 'feedback/feedback.html', {'error': 'Something Went Wrong'})


def faq(request):
    return render(request, 'faq/faq-1.html')


def invoice(request):
    return render(request, 'invoice-2.html')
