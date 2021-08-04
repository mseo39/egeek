from calendar import month
from django.db import models
import egeek.settings
import os
# Create your models here.

class Uploadfile(models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to='file/')
    chk=models.IntegerField(default=0,null=True)

    def delete(self, *args, **kargs):
        if self.file:
            os.remove(os.path.join(egeek.settings.MEDIA_ROOT, self.file.name))
        super(Uploadfile, self).delete(*args, **kargs)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.title
#향설
class dorm1_data(models.Model):
    dorm=models.CharField(max_length=10)
    dorm_number=models.CharField(max_length=10)
    student_number=models.CharField(max_length=10)
    qr_image=models.ImageField(null=True)
    file_name=models.CharField(max_length=10,null=True)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.dorm_number
    
    def delete(self, *args, **kargs):
        if self.qr_image:
            os.remove(os.path.join(egeek.settings.MEDIA_ROOT, self.qr_image))
            super(dorm1_data, self).delete(*args, **kargs)

class dorm2_data(models.Model):
    dorm=models.CharField(max_length=10)
    dorm_number=models.CharField(max_length=10)
    student_number=models.CharField(max_length=10)
    qr_image=models.ImageField(null=True)
    file_name=models.CharField(max_length=10,null=True)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.dorm_number

class dorm3_data(models.Model):
    dorm=models.CharField(max_length=10)
    dorm_number=models.CharField(max_length=10)
    student_number=models.CharField(max_length=10)
    qr_image=models.ImageField(null=True)
    file_name=models.CharField(max_length=10,null=True)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.dorm_number
#학성사
class old_dorm1_data(models.Model):
    dorm=models.CharField(max_length=10)
    dorm_number=models.CharField(max_length=10)
    student_number=models.CharField(max_length=10)
    qr_image=models.ImageField(null=True)
    file_name=models.CharField(max_length=10,null=True)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.dorm_number

class old_dorm2_data(models.Model):
    dorm=models.CharField(max_length=10)
    dorm_number=models.CharField(max_length=10)
    student_number=models.CharField(max_length=10)
    qr_image=models.ImageField(null=True)
    file_name=models.CharField(max_length=10,null=True)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.dorm_number

class old_dorm3_data(models.Model):
    dorm=models.CharField(max_length=10)
    dorm_number=models.CharField(max_length=10)
    student_number=models.CharField(max_length=10)
    qr_image=models.ImageField(null=True)
    file_name=models.CharField(max_length=10,null=True)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.dorm_number

#글로벌빌리지
class global_dorm_data(models.Model):
    dorm=models.CharField(max_length=10)
    dorm_number=models.CharField(max_length=10)
    student_number=models.CharField(max_length=10)
    qr_image=models.ImageField(null=True)
    file_name=models.CharField(max_length=10,null=True)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.dorm_number

class manager(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.username

class overnight_stay(models.Model):
    month=models.IntegerField(default=0)
    day=models.IntegerField(default=0)
    student_number=models.IntegerField()
    dorm=models.CharField(max_length=10)
    dorm_number=models.CharField(max_length=10)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.dorm_number

#기숙사명, 날짜, 호실
class overnight_list(models.Model):
    month=models.IntegerField()
    day=models.IntegerField()
    dorm=models.CharField(max_length=10)
    dorm_number=models.CharField(max_length=10)

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.dorm_number