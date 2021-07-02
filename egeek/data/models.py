from django.db import models

# Create your models here.

class Uploadfile(models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to='file/')

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.title