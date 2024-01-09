from django.db import models

# Create your models here.
class JobPost(models.Model):
    Job_Title = models.CharField(max_length=200)
    Job_Summary=models.CharField(max_length=200)
    Key_Responsibilities=models.CharField(max_length=200)
    Qualifications=models.CharField(max_length=200)
    Requirements=models.CharField(max_length=200)
    Skills_Competencies=models.CharField(max_length=200)
    Working_Conditions=models.CharField(max_length=200)
    Salary_and_Benefits=models.CharField(max_length=200)
    Application_Deadline=models.CharField(max_length=200)
    Location=models.CharField(max_length=200)
    Date_Posted=models.CharField(max_length=200)
    Expiration_Date=models.CharField(max_length=200)


