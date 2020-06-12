from django.shortcuts import render

from . models import SignUp,Personal_Info,Bike_Info

'''<a href="{% url 'Main:user_dashbord' %}" class="btn btn-primary btn-elevate kt-login__btn-primary">
											Sign Up </a>'''

class UserName:
    UserName=''
    def __init__(self):
        pass

def signup(request):
    if request.method == "GET":
        return render(request, 'login_pages/signup.html')
    else:

        Fname = request.POST['Fname']
        Lname=request.POST['Lname']
        Email = request.POST['Email']

        Password = request.POST['Password1']
        Password2 = request.POST['Password2']

        print(Email)
        if Password == Password2:
            User = SignUp(Fname=Fname, Lname=Lname , Email=Email, Password=Password)
            User.save()
            UserName.UserName=User.Email
            request.session.flush()
            request.session['username'] = UserName.UserName
            request.session['fname'] = User.Fname
            request.session['fullname'] = User.Fname+" "+User.Lname
            request.session['initial'] = User.getinitial()
            return render(request, 'user_dashbord.html')

        else:
            print('password dose not match ')
            return render(request, 'login_pages/signup.html')



def login(request):
    r = request.method
    print(r)
    print("hiiiiii")
    if request.method == "GET":
        return render(request, 'login_pages/login-1.html')
    else:
        Email = request.POST['Email']
        Password = request.POST['Password']
        print(Email)
        print(Password)
        try:
            go = SignUp.objects.get(Email=Email)
            UserName.UserName = go.Email
            print('2')
            psw = go.Password
            print(psw)
            if Password == psw:
                print('valid password')
                username = {'uname': Email }
                request.session['username'] = go.Email
                request.session['fname'] = go.Fname
                request.session['fullname'] = go.Fname+" "+go.Lname
                request.session['initial'] = go.getinitial()
                return render(request, 'user_dashbord.html')

            else:
                print('invalid password')
                return render(request, 'login_pages/login-1.html')


        except SignUp.DoesNotExist:
            print('invalid user name')
            return render(request, 'login_pages/login-1.html')
            go = None





def logout(request):
    request.session.flush()
    return render(request, 'login_pages/login-1.html')

def lockscreen(request):
    return render(request, 'login_pages/lockscreen.html')

def forget_password(request):
    return render(request, 'login_pages/forgetpassword.html')

#user Profile Settings
def personal_information(request):

    if request.method == 'GET':
        User= SignUp.objects.get(Email=UserName.UserName)
        Fname=User.Fname
        Lname=User.Lname
        Email=User.Email
        pic=Personal_Info.objects.get(Email__Email=UserName.UserName)
        Photo=pic.Profile_Pic
        phone=pic.Phone_no
        user={'Fname':Fname,'Lname':Lname,'Email':Email,'photo':Photo,'phone':phone}
        return render(request,'user_settings/profile-settings.html',user)
    else:
        Uname = request.POST['Uname']
        Profile_Pic = request.FILES['image']

        DOB = request.POST['DOB']
        Gender = request.POST['Gender']
        Phone_no = request.POST['Phone_no']
        Add_line1 = request.POST['Add_line1']
        Add_line2 = request.POST['Add_line2']
        City = request.POST['City']
        State = request.POST['State']
        Postal_Code = request.POST['Postal_Code']
        User = SignUp.objects.get(Email=UserName.UserName)
        Personal_info=Personal_Info(Email=User ,Profile_Pic=Profile_Pic,Uname=Uname,
                                    DOB=DOB,Gender=Gender,Phone_no=Phone_no,Add_line1=Add_line1,
                                    Add_line2=Add_line1,City=City,State=State,Postal_Code=Postal_Code)
        Personal_info.save()
        message={'msg':"uploded"}
        return render(request,'user_settings/profile-settings.html',message)



def account_information(request):
    return render(request, 'user_settings/account-information.html')

def bike_information(request):
    if request.method == "GET":
        Personal_info=Personal_Info.objects.get(Email__Email=UserName.UserName)

        Username={'Uname':Personal_info.Uname}
        return render(request,'user_settings/bike-info.html',Username)
    else:
        Bike_Model_Name = request.POST['Bike_Model_Name']
        Bike_No = request.POST['Bike_No']
        Bike_Reg_No = request.POST['Bike_Reg_No']
        Licence_No =request.POST['Licence_No']
        Licence = request.FILES['Licence']
        User = SignUp.objects.get(Email=UserName.UserName)
        Bike_info= Bike_Info(Email=User,Bike_Model_Name=Bike_Model_Name,
                             Bike_No=Bike_No,Bike_Reg_No=Bike_Reg_No,Licence_No=Licence_No,Licence=Licence)
        Bike_info.save()
        message={'msg':'Uplode'}
        return render(request, 'user_settings/bike-info.html',message)



def emergency_contact(request):
    if request.method == 'GET':
        a=1
        One={'one':a}
        return render(request,'user_settings/emergenci-contact.html',One)
    else:
        Primary = request.POST['Primary']
        Number = request.POST['Number']
        Full_Name=request.POST['FullName']
        Relations =request.POST['radio']


        print(Full_Name)
    return render(request, 'user_settings/emergenci-contact.html')

def change_password(request):
    return render(request, 'user_settings/change-password.html')

def email_setting(request):
    return render(request, 'user_settings/email-settings.html')

'''
background-image: url(&quot;http://keenthemes.com/metronic/preview/default/custom/user/assets/media/users/100_1.jpg&quot;);'''
