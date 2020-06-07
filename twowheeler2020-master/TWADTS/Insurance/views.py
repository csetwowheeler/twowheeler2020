from django.shortcuts import render

# Create your views here.
def add_insurance(request):
    return render(request, 'insurance/add-insurance.html')


def insurance_detail(request):
    return render(request, 'insurance/insurance-details.html')


def process_insurance(request):
    return render(request, 'insurance/claim-process/process-insurance.html')

def insurance_guidlines(request):

    return render(request, 'insurance/claim-process/guidlines.html')
