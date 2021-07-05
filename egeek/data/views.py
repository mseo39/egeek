from django.shortcuts import render, redirect
from .forms import uploadfile_form
import pandas as pd
from .models import Uploadfile, dorm1_data, dorm2_data,dorm3_data

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
    if(row[1][row[1].index[0]]=="향1"):
        dorm=dorm1_data()
    elif(row[1][row[1].index[0]]=="향2"):
        dorm=dorm2_data()
    elif(row[1][row[1].index[0]]=="향3"):
        dorm=dorm3_data()
    dorm.dorm=row[1][row[1].index[0]]
    dorm.dorm_number=row[1][row[1].index[1]]
    dorm.student_number=row[1][row[1].index[2]]
    dorm.save()
            
def select_file(request):
    if request.method=="POST":
        chk_file=request.POST.getlist('file[]')
        for file in chk_file:
            directory="media/file/{}.xlsx".format(file)
            df=pd.read_excel(directory, header=0)

            for row in df.iterrows():
                excel_to_db(row)

        return redirect("select_file")
    files=Uploadfile.objects.all()
    return render(request, 'file.html', {'files':files})

