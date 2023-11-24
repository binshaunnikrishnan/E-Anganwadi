from django.db import models

# Create your models here.

class login_table(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    type=models.CharField(max_length=90)

class staff_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=90)
    lastname=models.CharField(max_length=90)
    age=models.IntegerField()
    place=models.CharField(max_length=90)
    post=models.CharField(max_length=90)
    pin=models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=90)
    photo=models.FileField()

class student_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    STAFF = models.ForeignKey(staff_table, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=90)
    lastname = models.CharField(max_length=90)
    age = models.IntegerField()
    place = models.CharField(max_length=90)
    post = models.CharField(max_length=90)
    parentname = models.CharField(max_length=90)
    pin = models.BigIntegerField()
    phone = models.BigIntegerField()
    photo = models.FileField()
    email = models.CharField(max_length=90)

class workingtime_table(models.Model):
    fromtime=models.TimeField()
    totime=models.TimeField()
    date=models.DateField()

class fooditems_table(models.Model):
    fooditem=models.CharField(max_length=90)
    time=models.TimeField(max_length=90)
    day=models.CharField(max_length=100)

class syllabus_table(models.Model):
    subject=models.CharField(max_length=90)
    syllabus=models.FileField()

class anganwadi_table(models.Model):
    anganwadiname=models.CharField(max_length=90)
    photo=models.FileField()
    place=models.CharField(max_length=90)
    post=models.CharField(max_length=90)
    pin=models.BigIntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=90)

class complaints_table(models.Model):
    STUDENT = models.ForeignKey(student_table, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=90)
    date=models.DateField()
    reply=models.CharField(max_length=90)

class assign_table(models.Model):
    STAFF = models.ForeignKey(staff_table, on_delete=models.CASCADE)
    ANGANWADI = models.ForeignKey(anganwadi_table, on_delete=models.CASCADE)
    date=models.DateField()

class feedback_table(models.Model):
    feedback=models.CharField(max_length=90)
    date=models.DateField()
    rating=models.IntegerField()
    STUDENT = models.ForeignKey(student_table, on_delete=models.CASCADE)

class leaverequest_table(models.Model):
    STUDENT = models.ForeignKey(student_table, on_delete=models.CASCADE)
    date = models.DateField()
    levedate=models.DateField()
    request=models.CharField(max_length=90)

class chat_table(models.Model):
    fromid = models.ForeignKey(login_table, on_delete=models.CASCADE,related_name="a")
    toid = models.ForeignKey(login_table, on_delete=models.CASCADE,related_name="b")
    message=models.CharField(max_length=100)
    date=models.DateField()

class studymaterials_table(models.Model):
    STAFF = models.ForeignKey(staff_table, on_delete=models.CASCADE)
    studymaterials=models.FileField()
    title=models.CharField(max_length=90)


