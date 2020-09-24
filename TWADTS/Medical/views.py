from django.shortcuts import render
from .models import Medical_History
from Users.models import SignUp

from django.shortcuts import get_object_or_404
from  Users.views import UserName
# Create your views here.
def add_medical_detail(request):
    if request.method == 'GET':

        username = request.session['username']
        uname = {'Email':username}
        return render(request,'medical/add-medical-details.html', uname)
    else:
        print('1')
        Email = request.POST['Email']
        Complete_Name = request.POST['Name']
        Weight =request.POST['Weight']
        Hight = request.POST['Height']
        Blood_Pressure = request.POST['Blood_Pressure']
        Emergency_Contact = request.POST['Emergency_Contact']
        Address_Line1 = request.POST['Address1']
        Address_Line2 =request.POST['Address2']
        City = request.POST['City']
        State = request.POST['State']
        Postal_code = request.POST['Postal_Code']
        Past_Treatment = request.POST['PastTreatment']
        Past_Treatment_Description = request.POST['PastTreatmentDescription']
        Past_Report = request.FILES['PastTreatmentReport']
        Past_Injury = request.POST['PastInjuries']
        Past_Injury_Description = request.POST['PastInjuriesDescriptions']
        Past_Injury_Report = request.FILES['PastInjuriesReport']
        Genetic_Disorder = request.POST['GeneticDisorder']
        Genetic_Disorder_Description = request.POST['GeneticDisorderDescription']
        Genetic_Disorder_Report = request.FILES['GeneticDisorderReport']
        Ongoing_Medicine = request.POST['CurrentlyPursuingMedicine']
        Ongoing_Medicine_Description = request.POST['CurrentlyPursuingMedicineDescription']
        Ongoing_Medicine_Report =request.FILES['CurrentlyPursuingMedicineReport']
        Other_Details = request.POST['OtherDetails']
        Other_Details_Description = request.POST['OtherDetailsDescription']
        Other_Details_Report = request.FILES['OtherDetailsReport']
        uname = request.session['username']
        print("1")
        print('mac')

        user = get_object_or_404(SignUp, Email=uname)

        if uname == Email:
            try:

                print('2')


                print(user)


                # Medical_Data=Medical_History.objects.get(Email=user)\

                #
                #
                #
                # Medical_Data.Complete_Name =Complete_Name
                #
                # Medical_Data.Weight =Weight
                #
                # Medical_Data.Hight=Hight
                # Medical_Data.Blood_Pressure= Blood_Pressure
                #
                # Medical_Data.Emergency_Contact =Emergency_Contact
                #
                # Medical_Data.Address_Line=Address_Line1
                # Medical_Data.Address_Line2=Address_Line2
                # Medical_Data.City =City
                # Medical_Data.State=State
                # Medical_Data.Postal_code =Postal_code
                # Medical_Data.Past_Treatment=Past_Treatment
                # Medical_Data.Past_Treatment_Description=Past_Treatment_Description
                # Medical_Data.Past_Report=Past_Report
                #
                # Medical_Data.Past_Injury=Past_Injury
                #
                # Medical_Data.Past_Injury_Description=Past_Injury_Description
                # Medical_Data.Past_Injury_Report=Past_Injury_Report
                # Medical_Data.Genetic_Disorder=Genetic_Disorder
                #
                # Medical_Data.Genetic_Disorder_Description=Genetic_Disorder_Description
                # Medical_Data.Genetic_Disorder_Report=Genetic_Disorder_Report
                # Medical_Data.Ongoing_Medicine=Ongoing_Medicine
                #
                # Medical_Data.Ongoing_Medicine_Description=Ongoing_Medicine_Description
                # Medical_Data.Ongoing_Medicine_Report=Ongoing_Medicine_Report
                # Medical_Data.Other_Details=Other_Details
                # Medical_Data.Other_Details_Description=Other_Details_Description
                # Medical_Data.Other_Details_Report=Other_Details_Report

                Medical_Data = Medical_History.objects.get(Email=user)
                Medical_Data.Complete_Name = Complete_Name

                Medical_Data.Weight =Weight

                Medical_Data.Hight=Hight
                Medical_Data.Blood_Pressure= Blood_Pressure

                Medical_Data.Emergency_Contact =Emergency_Contact

                Medical_Data.Address_Line=Address_Line1
                Medical_Data.Address_Line2=Address_Line2
                Medical_Data.City =City
                Medical_Data.State=State
                Medical_Data.Postal_code =Postal_code
                Medical_Data.Past_Treatment=Past_Treatment
                Medical_Data.Past_Treatment_Description=Past_Treatment_Description
                Medical_Data.Past_Report=Past_Report

                Medical_Data.Past_Injury=Past_Injury

                Medical_Data.Past_Injury_Description=Past_Injury_Description
                Medical_Data.Past_Injury_Report=Past_Injury_Report
                Medical_Data.Genetic_Disorder=Genetic_Disorder

                Medical_Data.Genetic_Disorder_Description=Genetic_Disorder_Description
                Medical_Data.Genetic_Disorder_Report=Genetic_Disorder_Report
                Medical_Data.Ongoing_Medicine=Ongoing_Medicine

                Medical_Data.Ongoing_Medicine_Description=Ongoing_Medicine_Description
                Medical_Data.Ongoing_Medicine_Report=Ongoing_Medicine_Report
                Medical_Data.Other_Details=Other_Details
                Medical_Data.Other_Details_Description=Other_Details_Description
                Medical_Data.Other_Details_Report=Other_Details_Report

                Medical_Data.save()
                print('hii')

                # info = {'Email1': Email, 'Complete_Name': Complete_Name, 'Weight': Weight, 'Hight': Hight,
                #         'Blood_Pressure': Blood_Pressure, 'Emergency_Contact': Emergency_Contact,
                #         'Address_Line1': Address_Line1, 'Address_Line2': Address_Line2, 'City': City, 'State': State,
                #         'Postal_code': Postal_code, 'Past_Treatment': Past_Treatment,
                #         'Past_Treatment_Description': Past_Treatment_Description, 'Past_Report': Past_Report,
                #         'Past_Injury': Past_Injury, 'Past_Injury_Description': Past_Injury_Description,
                #         'Past_Injury_Report': Past_Injury_Report, 'Genetic_Disorder': Genetic_Disorder,
                #         'Genetic_Disorder_Description': Genetic_Disorder_Description,
                #         'Genetic_Disorder_Report': Genetic_Disorder_Report,
                #         'Ongoing_Medicine': Ongoing_Medicine,
                #         'Ongoing_Medicine_Description': Ongoing_Medicine_Description,
                #         'Ongoing_Medicine_Report': Ongoing_Medicine_Report,
                #         'Other_Details': Other_Details, 'Other_Details_Description': Ongoing_Medicine_Description,
                #         'Other_Details_Report': Other_Details_Report}
                return render(request, 'medical/add-medical-details.html')


            except Exception:

                Medical_data = Medical_History.objects.create(Email=user, Complete_Name=Complete_Name, Hight=Hight,
                                                              Weight=Weight, Blood_Pressure=Blood_Pressure,
                                                              Emergency_Contact=Emergency_Contact,
                                                              Address_Line1=Address_Line1, Address_Line2=Address_Line2,
                                                              City=City, State=State, Postal_code=Postal_code,
                                                              Past_Treatment=Past_Treatment,
                                                              Past_Treatment_Description=Past_Treatment_Description,
                                                              Past_Report=Past_Report,
                                                              Past_Injury=Past_Injury,
                                                              Past_Injury_Description=Past_Injury_Description,
                                                              Past_Injury_Report=Past_Injury_Report,
                                                              Genetic_Disorder=Genetic_Disorder,
                                                              Genetic_Disorder_Description=Genetic_Disorder_Description,
                                                              Genetic_Disorder_Report=Genetic_Disorder_Report,
                                                              Ongoing_Medicine=Ongoing_Medicine,
                                                              Ongoing_Medicine_Description=Ongoing_Medicine_Description,
                                                              Ongoing_Medicine_Report=Ongoing_Medicine_Report,
                                                              Other_Details=Other_Details,
                                                              Other_Details_Description=Other_Details_Description,
                                                              Other_Details_Report=Other_Details_Report)
                Medical_data.save()

                print('3')
                info = {'Email1': Email, 'Complete_Name': Complete_Name, 'Weight': Weight, 'Hight': Hight,
                        'Blood_Pressure': Blood_Pressure, 'Emergency_Contact': Emergency_Contact,
                        'Address_Line1': Address_Line1, 'Address_Line2': Address_Line2, 'City': City, 'State': State,
                        'Postal_code': Postal_code, 'Past_Treatment': Past_Treatment,
                        'Past_Treatment_Description': Past_Treatment_Description, 'Past_Report': Past_Report,
                        'Past_Injury': Past_Injury, 'Past_Injury_Description': Past_Injury_Description,
                        'Past_Injury_Report': Past_Injury_Report, 'Genetic_Disorder': Genetic_Disorder,
                        'Genetic_Disorder_Description': Genetic_Disorder_Description,
                        'Genetic_Disorder_Report': Genetic_Disorder_Report,
                        'Ongoing_Medicine': Ongoing_Medicine,
                        'Ongoing_Medicine_Description': Ongoing_Medicine_Description,
                        'Ongoing_Medicine_Report': Ongoing_Medicine_Report,
                        'Other_Details': Other_Details, 'Other_Details_Description': Ongoing_Medicine_Description,
                        'Other_Details_Report': Other_Details_Report}

                return render(request, 'medical/add-medical-details.html',info)


def medical_history(request):
    if request.method == 'GET':
        try:

            Medical_Data=Medical_History.objects.get(Email=request.session['username'])
            Email = Medical_Data.Email
            print(Email)
            Complete_Name  = Medical_Data.Complete_Name

            Weight = Medical_Data.Weight

            Hight = Medical_Data.Hight
            Blood_Pressure = Medical_Data.Blood_Pressure

            Emergency_Contact = Medical_Data.Emergency_Contact

            Address_Line1 = Medical_Data.Address_Line1
            Address_Line2 = Medical_Data.Address_Line2
            City = Medical_Data.City
            State = Medical_Data.State
            Postal_code = Medical_Data.Postal_code
            Past_Treatment = Medical_Data.Past_Treatment
            Past_Treatment_Description = Medical_Data.Past_Treatment_Description
            Past_Report = Medical_Data.Past_Report

            Past_Injury = Medical_Data.Past_Injury

            Past_Injury_Description = Medical_Data.Past_Injury_Description
            Past_Injury_Report = Medical_Data.Past_Injury_Report
            Genetic_Disorder = Medical_Data.Genetic_Disorder

            Genetic_Disorder_Description = Medical_Data.Genetic_Disorder_Description
            Genetic_Disorder_Report = Medical_Data.Genetic_Disorder_Report
            Ongoing_Medicine = Medical_Data.Ongoing_Medicine

            Ongoing_Medicine_Description = Medical_Data.Ongoing_Medicine_Description
            Ongoing_Medicine_Report = Medical_Data.Ongoing_Medicine_Report
            Other_Details = Medical_Data.Other_Details
            Other_Details_Description = Medical_Data.Other_Details_Description
            Other_Details_Report = Medical_Data.Other_Details_Report

            info = { 'Email1': Email,'Complete_Name' : Complete_Name, 'Weight': Weight ,'Hight':Hight, 'Blood_Pressure':Blood_Pressure, 'Emergency_Contact':Emergency_Contact,
                'Address_Line1':Address_Line1,'Address_Line2':Address_Line2,'City':City, 'State':State ,'Postal_code':Postal_code,'Past_Treatment':Past_Treatment,
                'Past_Treatment_Description':Past_Treatment_Description,'Past_Report':Past_Report,'Past_Injury':Past_Injury,'Past_Injury_Description':Past_Injury_Description,
                'Past_Injury_Report':Past_Injury_Report,'Genetic_Disorder':Genetic_Disorder,'Genetic_Disorder_Description':Genetic_Disorder_Description,'Genetic_Disorder_Report':Genetic_Disorder_Report,
                'Ongoing_Medicine':Ongoing_Medicine,'Ongoing_Medicine_Description':Ongoing_Medicine_Description,'Ongoing_Medicine_Report':Ongoing_Medicine_Report,
                'Other_Details':Other_Details,'Other_Details_Description':Ongoing_Medicine_Description,'Other_Details_Report':Other_Details_Report }

            return render(request, 'medical/medical-history.html',info)

        except Exception:

            return render(request, 'medical/medical-history.html')


''''Complete_Name': Complete_Name, 'Weight': Weight , 'Blood_Pressure':Blood_Pressure, 'Emergency_Contact':Emergency_Contact,
                'Address_Line1':Address_Line1,'Address_Line2':Address_Line2,'City':City, 'State':State ,'Postal_code':Postal_code,'Past_Treatment':Past_Treatment,
                'Past_Treatment_Description':Past_Treatment_Description,'Past_Report':Past_Report,'Past_Injury':Past_Injury,'Past_Injury_Description':Past_Injury_Description,
                'Past_Injury_Report':Past_Injury_Report,'Genetic_Disorder':Genetic_Disorder,'Genetic_Disorder_Description':Genetic_Disorder_Description,'Genetic_Disorder_Report':Genetic_Disorder_Report,
                'Ongoing_Medicine':Ongoing_Medicine,'Ongoing_Medicine_Description':Ongoing_Medicine_Description,'Ongoing_Medicine_Report':Ongoing_Medicine_Report,
                'Other_Details':Other_Details,'Other_Details_Description':Ongoing_Medicine_Description,'Other_Details_Report':Other_Details_Report '''