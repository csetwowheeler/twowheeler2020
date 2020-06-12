from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from datetime import datetime
from django.core.files.storage import FileSystemStorage

from Users.models import SignUp
from Insurance.models import Insurance

# Create your views here.
def add_insurance(request):
    return render(request, 'insurance/add-insurance.html')


def insurance_detail(request):
    return render(request, 'insurance/insurance-details.html')


def process_insurance(request):
    return render(request, 'insurance/claim-process/process-insurance.html')

def insurance_guidlines(request):

    return render(request, 'insurance/claim-process/guidlines.html')

def save_info(request):
    if request.method == 'POST':
        email = request.session['username']
        user = get_object_or_404(SignUp, Email=email)

        id = int(request.POST['id'])
        insurance_id = request.POST['insurance_id']
        policy_no = request.POST['policy_no']
        insurance_type = request.POST['insurance_type']
        carrier_type = request.POST['carrier_type']
        startdate = request.POST['startdate']
        startdate=datetime.strptime(startdate,'%m/%d/%Y').date()
        enddate = request.POST['enddate']
        enddate=datetime.strptime(enddate,'%m/%d/%Y').date()
        insurance_carrycode = int(request.POST['insurance_carrycode'])
        insurance_doc = request.FILES['doc']
        fs = FileSystemStorage()
        file = fs.save(insurance_doc.name, insurance_doc)
        # Ins = Insurance.objects.create(user=user,insurance_id=insurance_id,policy_no=policy_no,insurance_type=insurance_type,carrier_type=carrier_type,startdate=startdate,enddate=enddate,insurance_carrycode=insurance_carrycode,insurance_doc=file)
        # Ins.save()

        context_stuff ={
            'user': user,
            'id': id,
            'insurance_id':insurance_id,
            'policy_no': policy_no,
            'insurance_type': insurance_type,
            'carrier_type': carrier_type,
            'startdate': startdate,
            'enddate': enddate,
            'insurance_carrycode': insurance_carrycode,
            'insurance_doc': insurance_doc,
            'url':url
        }
        for data in context_stuff.values():
            print(data,type(data))


        return HttpResponseRedirect('insurance/add-insurance.html')
