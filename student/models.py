from django.db import models
import datetime
# Create your models here.
class Profile(models.Model):
    image=models.ImageField(upload_to='pics',height_field=None, width_field=None, max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.date.today )
    end_date = models.DateField(default=datetime.date.today)
    College = models.CharField (max_length=100)
    degree = models. CharField(max_length=100)
    skill=models.TextField (max_length=1000)
    about_you=models.TextField(max_length=1000)
    previous_work=models.TextField(max_length=1000)
    projects = models.CharField(max_length=1000)
    project_desc = models.TextField()

