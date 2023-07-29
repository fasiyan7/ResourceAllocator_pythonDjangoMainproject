from django.db import models
from django.contrib.auth.models import AbstractUser
# Three type users
class CustomUser(AbstractUser):
    USER=(
        ('1','ADMIN'),
        ('2','STAFF'),
        ('3','STUDENT'),
    )
    user_type=models.CharField(choices=USER, max_length=200,default=3)
    profile_pic = models.ImageField(upload_to='media/profile_pic',null=True,blank=True) 
    def __str__(self):
        return self.username
class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)


    def __str__(self):
        return self.session_start + " To " + self.session_end
class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
		
	#staff panel

class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    phone=models.IntegerField(null=True,blank=True)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username
    

class Laptop(models.Model):
    lapname=models.CharField(max_length=200)
    def __str__(self):
        return self.lapname
class Hall(models.Model):
    hallname=models.CharField(max_length=20)
    def __str__(self):
        return self.hallname


class Batches(models.Model):
    batchname = models.CharField(max_length=255,null=True,blank=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1) #need to give defauult course
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE,default=1)
    laptop_id = models.ForeignKey(Laptop, on_delete=models.CASCADE,default=1) #need to give defauult course
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE,default=1) #need to give defauult course
   # admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    #starttime=models.DateTimeField(auto_now_add=True)
   # endtime=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.batchname
    #pending -show the student list ,showing start date and end date

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.title
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    assigntopic = models.FileField(upload_to = 'Assignment')   
    created = models.DateField(auto_now_add=False)
    enddate = models.DateField(auto_now_add=False)


    def __str__(self):
        return self.title

class MarkList(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)
    marks_math = models.DecimalField(max_digits=5, decimal_places=2)
    marks_science = models.DecimalField(max_digits=5, decimal_places=2)
    marks_english = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name




  


    
