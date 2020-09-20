from django.shortcuts import render

from . models import SignUp, Personal_Info, Bike_Info, Emergency_Contact, Account_Info

'''<a href="{% url 'Main:user_dashbord' %}" class="btn btn-primary btn-elevate kt-login__btn-primary">
											Sign Up </a>'''


class UserName:
    UserName = ''

    def __init__(self):
        pass


def signup(request):
    if request.method == "GET":
        return render(request, 'login_pages/signup.html')
    else:

        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        Email = request.POST['Email']

        Password = request.POST['Password1']
        Password2 = request.POST['Password2']

        print(Email)
        if Password == Password2:
            User = SignUp(Fname=Fname, Lname=Lname,
                          Email=Email, Password=Password)
            User.save()
            UserName.UserName = User.Email
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
                username = {'uname': Email}
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

# user Profile Settings


def personal_information(request):
    User = SignUp.objects.get(Email=request.session['username'])
    Fname = User.Fname
    Lname = User.Lname
    Email = User.Email

    if request.method == 'GET':

        try:

            pic = Personal_Info.objects.get(
                Email__Email=request.session['username'])
            Photo = pic.Profile_Pic
            print(Photo)
            phone = pic.Phone_no
            Uname = pic.Uname

            print(phone)
            DOB = pic.DOB
            Add_line1 = pic.Add_line1
            Add_line2 = pic.Add_line2
            City = pic.City
            State = pic.State
            Postal_Code = pic.Postal_Code
            print('2')
            user = {'Fname': Fname, 'Lname': Lname, 'Email': Email, 'Uname': Uname, 'photo': Photo, 'phone': phone,
                    'Add_line1': Add_line1, 'Add_line2': Add_line2, 'City': City, 'State': State, 'Postal_Code': Postal_Code}
            print('3')
            return render(request, 'user_settings/profile-settings.html', user)
        except Exception:
            user = {'Fname': Fname, 'Lname': Lname, 'Email': Email, }
            return render(request, 'user_settings/profile-settings.html', user)

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
        User = SignUp.objects.get(Email=request.session['username'])
        Fname = User.Fname
        Lname = User.Lname
        Email = User.Email
        try:
            pic = Personal_Info.objects.get(
                Email__Email=request.session['username'])
            pic.Profile_Pic = Profile_Pic
            pic.Phone_no = Phone_no
            pic.Gender = Gender
            pic.Add_line1 = Add_line1
            pic.Add_line2 = Add_line2
            pic.City = City
            pic.State = State
            pic.Postal_Code = Postal_Code
            pic.save()

            user = {'msg': "uploded", 'Fname': Fname, 'Lname': Lname, 'Uname': Uname, 'Email': Email, 'DOB': DOB, 'photo': Profile_Pic, 'phone': Phone_no, 'Add_line1': Add_line1,
                    'Add_line2': Add_line2, 'City': City, 'State': State, 'Postal_Code': Postal_Code, 'Gender': Gender}

            return render(request, 'user_settings/profile-settings.html', user)
        except Exception:

            User = SignUp.objects.get(Email=UserName.UserName)
            print(User)
            Info = Personal_Info(Email=User, Uname=Uname, Profile_Pic=Profile_Pic, DOB=DOB, Gender=Gender, Phone_no=Phone_no, Add_line1=Add_line1,
                                 Add_line2=Add_line2, City=City, State=State, Postal_Code=Postal_Code)
            Info.save()

            message = {'msg': "uploded", 'Fname': Fname, 'Lname': Lname, 'Email': Email, 'Uname': Uname, 'photo': Profile_Pic, 'phone': Phone_no, 'Add_line1': Add_line1,
                       'Add_line2': Add_line2, 'City': City, 'State': State, 'Postal_Code': Postal_Code}
            return render(request, 'user_settings/profile-settings.html', message)


def account_information(request):
    User = SignUp.objects.get(Email=request.session['username'])
    Fname = User.Fname
    Lname = User.Lname
    if request.method == 'GET':
        print('1')
        try:
            User = Account_Info.objects.get(
                Email__Email=request.session['username'])
            print(User)
            Number = User.Number
            Full_Name = User.Full_Name
            try:
                print('2')
                pic = Personal_Info.objects.get(
                    Email__Email=request.session['username'])
                Photo = pic.Profile_Pic
                phone = pic.Phone_no

                print('3')
                info = {'photo': Photo, 'phone': phone, 'Email': User, 'Fname': Fname,
                        'Lname': Lname, 'number': Number,  'fullname': Full_Name, }
                return render(request, 'user_settings/account-information.html', info)
            except Exception:
                print('4')
                info = {'number': Number,  'fullname': Full_Name, 'Email': User,
                        'Fname': Fname, 'Lname': Lname, }
                return render(request, 'user_settings/account-information.html', info)
        except Exception:
            info = {'Email': User, 'Fname': Fname, 'Lname': Lname, }
            return render(request, 'user_settings/account-information.html', info)
    else:
        Number = request.POST['Number']
        Full_Name = request.POST['Name']
        print(Number)
        try:
            User = Account_Info.objects.get(
                Email__Email=request.session['username'])
            User.Number = Number
            User.Full_Name = Full_Name
            User.save()
            try:
                print('1')
                pic = Personal_Info.objects.get(
                    Email__Email=request.session['username'])
                Photo = pic.Profile_Pic
                phone = pic.Phone_no

                print('2')
                info = {'msg': "Uploaded", 'number': Number, 'fullname': Full_Name, 'photo': Photo, 'phone': phone, 'Email': User,
                        'Fname': Fname, 'Lname': Lname}
                return render(request, 'user_settings/account-information.html', info)
            except Exception:
                info = {'msg': "Uploaded", 'number': Number, 'fullname': Full_Name,
                        'Email': User,
                        'Fname': Fname, 'Lname': Lname}
                return render(request, 'user_settings/account-information.html', info)

        except Exception:

            contact = Account_Info(
                Email=User, Full_Name=Full_Name, Number=Number)
            contact.save()
            try:
                pic = Personal_Info.objects.get(
                    Email__Email=request.session['username'])
                Photo = pic.Profile_Pic
                phone = pic.Phone_no
                info = {'msg': "Uploaded", 'number': Number, 'fullname': Full_Name, 'photo': Photo, 'phone': phone,
                        'Email': User, 'Fname': Fname, 'Lname': Lname}
                return render(request, 'user_settings/account-information.html', info)
            except Exception:
                info = {'number': Number, 'fullname': Full_Name, 'Email': User,
                        'Fname': Fname, 'Lname': Lname, }
                return render(request, 'user_settings/account-information.html', info)


def bike_information(request):

    User = SignUp.objects.get(Email=request.session['username'])
    Fname = User.Fname
    Lname = User.Lname
    if request.method == "GET":

        try:
            Bike_info = Bike_Info.objects.get(
                Email__Email=request.session['username'])
            User = Bike_info.Email
            Bike_Model_Name = Bike_info.Bike_Model_Name
            Bike_No = Bike_info.Bike_No
            Bike_Reg_No = Bike_info.Bike_Reg_No
            Licence_No = Bike_info.Licence_No
            Licence = Bike_info.Licence
            try:
                pic = Personal_Info.objects.get(
                    Email__Email=request.session['username'])
                Photo = pic.Profile_Pic
                phone = pic.Phone_no
                info = {'Email': User, 'Bike_Model_Name': Bike_Model_Name, 'Bike_Reg_No': Bike_Reg_No,
                        'Bike_No': Bike_No, 'Licence': Licence, 'Licence_No': Licence_No, 'photo': Photo, 'phone': phone, 'Fname': Fname, 'Lname': Lname, }
                return render(request, 'user_settings/bike-info.html', info)

            except:
                info = {'Email': User, 'Bike_Model_Name': Bike_Model_Name, 'Bike_Reg_No': Bike_Reg_No,
                        'Bike_No': Bike_No, 'Licence': Licence, 'Licence_No': Licence_No,
                        'Fname': Fname, 'Lname': Lname, }
                return render(request, 'user_settings/bike-info.html', info)

        except Exception:
            info = {'Email': User, 'Fname': Fname, 'Lname': Lname, }
            return render(request, 'user_settings/account-information.html', info)

    else:
        Bike_Model_Name = request.POST['Bike_Model_Name']
        Bike_No = request.POST['Bike_No']
        Bike_Reg_No = request.POST['Bike_Reg_No']
        Licence_No = request.POST['Licence_No']
        Licence = request.FILES['Licence']
        User = SignUp.objects.get(Email=request.session['username'])
        try:
            Bike_info = Bike_Info.objects.get(
                Email__Email=request.session['username'])
            Bike_info.Bike_Model_Name = Bike_Model_Name
            Bike_info.Bike_No = Bike_No
            Bike_info.Bike_Reg_No = Bike_Reg_No
            Bike_info.Licence_No = Licence_No
            Bike_info.Licence = Licence
            Bike_info.save()
            try:
                pic = Personal_Info.objects.get(
                    Email__Email=request.session['username'])
                Photo = pic.Profile_Pic
                phone = pic.Phone_no
                info = {'msg': 'Uplode', 'Email': User, 'Bike_Model_Name': Bike_Model_Name, 'Bike_Reg_No': Bike_Reg_No,
                        'Bike_No': Bike_No, 'Licence': Licence, 'Licence_No': Licence_No, 'photo': Photo, 'phone': phone, 'Fname': Fname, 'Lname': Lname, }
                return render(request, 'user_settings/bike-info.html', info)
            except Exception:
                info = {'msg': 'Uplode', 'Email': User, 'Bike_Model_Name': Bike_Model_Name, 'Bike_Reg_No': Bike_Reg_No,
                        'Bike_No': Bike_No, 'Licence': Licence, 'Licence_No': Licence_No,  'Fname': Fname, 'Lname': Lname, }
                return render(request, 'user_settings/bike-info.html', info)

        except Exception:

            Bike_info = Bike_Info(Email=User, Bike_Model_Name=Bike_Model_Name,
                                  Bike_No=Bike_No, Bike_Reg_No=Bike_Reg_No, Licence_No=Licence_No, Licence=Licence)
            Bike_info.save()
            message = {'msg': 'Uplode', 'Email': User, 'Bike_Model_Name': Bike_Model_Name, 'Bike_Reg_No': Bike_Reg_No,
                       'Bike_No': Bike_No, 'Licence': Licence, 'Licence_No': Licence_No}
            return render(request, 'user_settings/bike-info.html', message)


def emergency_contact(request):

    User = SignUp.objects.get(Email=request.session['username'])
    Fname = User.Fname
    Lname = User.Lname
    print('1')
    if request.method == 'GET':
        try:
            print('2')
            emergency = Emergency_Contact.objects.get(
                Email__Email=request.session['username'])
            print(emergency)
            Number = emergency.Number
            Relations = emergency.Relations
            Full_Name = emergency.Full_Name
            print(Full_Name)

            try:
                print('3')
                pic = Personal_Info.objects.get(
                    Email__Email=request.session['username'])
                Photo = pic.Profile_Pic
                phone = pic.Phone_no
                info = {'msg': "Uploaded", 'number': Number, 'Relation': Relations, 'fullname': Full_Name,
                        'photo': Photo, 'phone': phone, 'Fname': Fname, 'Lname': Lname, 'Email': User}
                return render(request, 'user_settings/emergenci-contact.html', info)
            except Exception:
                info = {'msg': "Uploaded", 'number': Number, 'Relation': Relations, 'fullname': Full_Name,
                        'Fname': Fname, 'Lname': Lname, 'Email': User}
                return render(request, 'user_settings/emergenci-contact.html', info)

        except Exception:
            info = {'Fname': Fname, 'Lname': Lname, 'Email': User}
            return render(request, 'user_settings/emergenci-contact.html', info)

    else:

        Number = request.POST['Number']
        Full_Name = request.POST['FullName']
        Relationship = request.POST['radio']
        try:
            emergency = Emergency_Contact.objects.get(
                Email__Email=request.session['username'])
            print(emergency)
            emergency.Number = Number
            emergency.Relationship = Relationship
            emergency.Full_Name = Full_Name
            emergency.save()
            try:
                pic = Personal_Info.objects.get(
                    Email__Email=request.session['username'])
                Photo = pic.Profile_Pic
                phone = pic.Phone_no

                info = {'msg': "Uploaded", 'number': Number, 'Relation': Relationship, 'fullname': Full_Name,
                        'Fname': Fname, 'Lname': Lname, 'Email': User, 'photo': Photo, 'phone': phone}
                return render(request, 'user_settings/emergenci-contact.html', info)
            except Exception:
                info = {'msg': "Uploaded", 'number': Number, 'Relation': Relationship, 'fullname': Full_Name,
                        'Fname': Fname, 'Lname': Lname, 'Email': User, }
                return render(request, 'user_settings/emergenci-contact.html', info)

        except Exception:
            contact = Emergency_Contact(
                Email=User, Full_Name=Full_Name, Relationship=Relationship, Number=Number)
            contact.save()
            info = {'msg': "Uploaded", 'number': Number, 'Relation': Relationship,
                    'fullname': Full_Name, 'Fname': Fname, 'Lname': Lname, 'Email': User}
            return render(request, 'user_settings/emergenci-contact.html', info)


def change_password(request):

    return render(request, 'user_settings/change-password.html')


def email_setting(request):
    return render(request, 'user_settings/email-settings.html')


'''
background-image: url(&quot;http://keenthemes.com/metronic/preview/default/custom/user/assets/media/users/100_1.jpg&quot;);'''
