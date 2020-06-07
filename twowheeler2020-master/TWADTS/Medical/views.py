from django.shortcuts import render

# Create your views here.
def add_medical_detail(request):
    if request.method == 'GET':
        return render(request,'medical/add-medical-details.html')
    else:
        id = request.POST['id']
        name = request.POST['name']
        print(id)
        print('name')
        return render(request, 'medical/add-medical-details.html')







def medical_history(request):
    print('1')

    return render(request, 'medical/medical-history.html')
