

from django.db import models
from Users.models import SignUp


class Medical_History(models.Model):
    Email = models.ForeignKey(SignUp,on_delete=models.CASCADE,unique=True)
    Complete_Name= models.CharField(max_length=50)
    Weight=models.CharField(max_length=50)
    Hight = models.CharField(max_length=50)
    Blood_Pressure = models.CharField(max_length=50)
    Emergency_Contact= models.CharField(max_length=50)
    Address_Line1 = models.CharField(max_length=100)
    Address_Line2 = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State= models.CharField(max_length=50)
    Postal_code = models.CharField(max_length=50)
    Past_Treatment = models.CharField(max_length=10)
    Past_Treatment_Description = models.CharField(max_length=150)
    Past_Report= models.FileField(upload_to='Medical/Past_Report')
    Past_Injury = models.CharField(max_length=10)
    Past_Injury_Description = models.CharField(max_length=150)
    Past_Injury_Report = models.FileField(upload_to='Medical/Past_Injury_Report')
    Genetic_Disorder= models.CharField(max_length=10)
    Genetic_Disorder_Description=models.CharField(max_length=150)
    Genetic_Disorder_Report= models.FileField(upload_to="Medical/Genetic_Disorder_Report")
    Ongoing_Medicine = models.CharField(max_length=50)
    Ongoing_Medicine_Description= models.CharField(max_length=150)
    Ongoing_Medicine_Report = models.FileField(upload_to='Medical/Ongoing_Medicine_Report')
    Other_Details = models.CharField(max_length=10)
    Other_Details_Description = models.CharField(max_length=150)
    Other_Details_Report = models.FileField(upload_to='Medical/Other_Detail_Report')

    def __str__(self):
        return self.Complete_Name
