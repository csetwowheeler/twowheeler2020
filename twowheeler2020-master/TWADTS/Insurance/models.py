from django.db import models
from Users.models import SignUp

# Create your models here.
class Insurance(models.Model):
    user = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    insurance_id = models.IntegerField()
    policy_no = models.CharField(max_length=200)
    insurance_type = models.CharField(max_length=200)
    carrier_type = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField()
    insurance_carrycode = models.IntegerField()
    insurance_doc = models.FileField(upload_to='insurance_doc')

    def __str__(self):
        return self.insurance_type
