from django.db import models

# Create your models

class SignUp(models.Model):

     Fname = models.CharField(max_length=500)
     Lname = models.CharField(max_length=50)
     Email= models.CharField(max_length=50, primary_key=True)
     Password = models.CharField(max_length=50)

     def __str__(self):
          return self.Email

     def getinitial(self):
         return self.Fname[0]


class Personal_Info(models.Model):
     Email = models.ForeignKey(SignUp, on_delete=models.CASCADE , unique=True)
     Profile_Pic = models.ImageField(upload_to='Profile_Pic' , blank=True)
     Uname = models.CharField(max_length=50)
     DOB = models.CharField(max_length=50)
     Gender = models.CharField(max_length=50)
     Phone_no = models.IntegerField()
     Add_line1 = models.CharField(max_length=200)
     Add_line2 = models.CharField(max_length=200)
     City = models.CharField(max_length=50)
     State = models.CharField(max_length=50)
     Postal_Code = models.IntegerField()

     def __str__(self):
          return self.Uname

class Bike_Info(models.Model):
     Email = models.ForeignKey(SignUp, on_delete=models.CASCADE , unique=True)
     Bike_Model_Name = models.CharField(max_length=50)
     Bike_No = models.CharField(max_length=50)
     Bike_Reg_No =models.CharField(max_length=50)
     Licence_No = models.CharField(max_length=50)
     Licence = models.FileField(upload_to='Licence')

     def __str__(self):
          return self.Bike_No


class Emergency_Contact(models.Model):
     Email=models.ForeignKey(SignUp, on_delete=models.CASCADE, unique=True)
     Full_Name=models.CharField(max_length=50)
     Relationship=models.CharField(max_length=50)
     Number=models.CharField(max_length=10)

     def __str__(self):
          return self.Full_Name

class Account_Info(models.Model):
     Email=models.ForeignKey(SignUp,on_delete=models.CASCADE, unique=True)
     Full_Name=models.CharField(max_length=50)
     Number=models.CharField(max_length=10)

     def __str__(self):
          return self.Full_Name