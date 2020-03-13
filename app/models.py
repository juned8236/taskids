from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class  TestTable(models.Model):
    customerID = models.CharField(max_length = 255,null=True, blank=True)
    gender= models.CharField(max_length = 255,null=True, blank=True)
    SeniorCitizen= models.IntegerField(null=True, blank=True)
    Partner= models.CharField(max_length = 255,null=True, blank=True)
    Dependents= models.CharField(max_length = 255,null=True, blank=True)
    tenure= models.IntegerField(null=True, blank=True)
    PhoneService= models.CharField(max_length = 255,null=True, blank=True)
    MultipleLines= models.CharField(max_length = 255,null=True, blank=True)
    InternetService= models.CharField(max_length = 255,null=True, blank=True)
    OnlineSecurity= models.CharField(max_length = 255,null=True, blank=True)
    OnlineBackup= models.CharField(max_length = 255,null=True, blank=True)
    DeviceProtection= models.CharField(max_length = 255,null=True, blank=True)
    TechSupport= models.CharField(max_length = 255,null=True, blank=True)
    StreamingTV= models.CharField(max_length = 255,null=True, blank=True)
    StreamingMovies= models.CharField(max_length = 255,null=True, blank=True)
    Contract= models.CharField(max_length = 255,null=True, blank=True)
    PaperlessBilling= models.CharField(max_length = 255,null=True, blank=True)
    PaymentMethod= models.CharField(max_length = 255,null=True, blank=True)
    MonthlyCharges=models.IntegerField(null=True, blank=True)
    TotalCharges= models.IntegerField(null=True, blank=True)
    Churn= models.CharField(max_length = 255,null=True, blank=True)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length = 255,null=True, blank=True)
    password=models.CharField(max_length = 255,null=True, blank=True)