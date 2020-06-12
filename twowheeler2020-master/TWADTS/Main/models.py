from django.db import models
from Users.models import SignUp

# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(SignUp, on_delete=models.CASCADE, unique=True)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=500)
    suggestion = models.CharField(max_length=500)
    issue = models.CharField(max_length=500)

    def __str__(self):
        return self.user.Email
