from django.shortcuts import render, redirect
from .forms import uploadfile_form
import pandas as pd
from .models import Uploadfile, dorm1_data, dorm2_data,dorm3_data
from pyspark.sql import Row
from pyspark.sql import SparkSession
# Create your views here.
from pyspark import SparkContext
from pyspark.sql import SQLContext 
sc = SparkContext.getOrCreate() 
sql = SQLContext(sc)

def data(request):
    return render(request, 'main.html')

def upload_file(request):
    if request.method=="POST":
        form=uploadfile_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload_file")

    file_form=uploadfile_form()
    return render(request, 'main.html', {'file_form':file_form})

def excel_to_db(row):
    row=row.asDict()
    for key, value in row.items():
        if(key=="기숙사"):
            dorm=dorm1_data()
            dorm.dorm=value
        elif(key=="호실"):
            dorm.dorm_number=value
        elif(key=="학번"):
            dorm.student_number=value
            
def select_file(request):
    if request.method=="POST":
        chk_file=request.POST.getlist('file[]')
        for file in chk_file:
            directory="media/file/{}.xlsx".format(file)
            df=pd.read_excel(directory, header=0)

        return redirect("select_file")
    files=Uploadfile.objects.all()
    return render(request, 'file.html', {'files':files})

