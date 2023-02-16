from django.db import models
from django.utils import timezone
from django  import forms

class UsersData(models.Model):
    userName = models.CharField(max_length=120, blank=True)
    email = models.EmailField(max_length=200,unique=True, primary_key=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    create_at = models.DateField(default = timezone.now)

class UsersInfo(models.Model):
    job_title = models.CharField(max_length=30, null=True)
    spacificTitle = models.CharField(max_length=30, default="")
    department = models.CharField(max_length=130)
    currently_job_title = models.CharField(max_length=130)
    date_reviced_title = models.DateField(null=True)
    targeted_title = models.CharField(max_length=30)
    request_status = models.CharField(max_length=50, default="New")
    validation_date = models.DateField()
    requested_date = models.DateField(default= timezone.now)
    users = models.ForeignKey(UsersData,related_name='user_info', on_delete=models.CASCADE)
    
class FilesForms(models.Model):
    title = models.CharField(max_length=500)
    files_path = models.FileField(upload_to='files/', blank=True,null=True)
    user = models.ForeignKey(UsersInfo, on_delete=models.CASCADE)