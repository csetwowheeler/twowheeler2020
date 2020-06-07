from django.db import models

# Create your models here.
class Insurance(models.Model):
    insurance_detail = models.CharField(max_length=200)
    insurance_id = models.IntegerField()
    company_name = models.CharField(max_length=200)
    insurance_type = models.CharField(max_length=200)
    

    class Meta:
        verbose_name = ("Insurance")
        verbose_name_plural = ("Insurances")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Insurance_detail", kwargs={"pk": self.pk})
