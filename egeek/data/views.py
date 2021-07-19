from django.shortcuts import get_object_or_404, render, redirect
from .forms import uploadfile_form
import pandas as pd
from .models import Uploadfile, dorm1_data, dorm2_data,dorm3_data
import qrcode

def main(request):
    return render(request, 'home.html')

def detail(request,dorm, student_number):
    if(dorm=="향1"):
        dorm_= get_object_or_404(dorm1_data, student_number=student_number)
    elif(dorm=="향2"):
        dorm_= get_object_or_404(dorm2_data, student_number=student_number)
    elif(dorm=="향3"):
        dorm_= get_object_or_404(dorm3_data, student_number=student_number)
    return render(request, 'detail.html', {'dorm_data' : dorm_})

def upload_file(request):
    if request.method=="POST":
        form=uploadfile_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload_file")

    file_form=uploadfile_form()
    return render(request, 'main.html', {'file_form':file_form})

def excel_to_db(row,file):
    if(row[1][row[1].index[0]]=="향1"):
        dorm=dorm1_data()
    elif(row[1][row[1].index[0]]=="향2"):
        dorm=dorm2_data()
    elif(row[1][row[1].index[0]]=="향3"):
        dorm=dorm3_data()
    dorm.dorm=row[1][row[1].index[0]]
    dorm.dorm_number=row[1][row[1].index[1]]
    dorm.student_number=row[1][row[1].index[2]]
    dorm.file_name=file

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data('http://127.0.0.1:8000/')
    qr.add_data('detail/'+row[1][row[1].index[0]]+'/')
    qr.add_data(row[1][row[1].index[2]])
    img = qr.make_image(fill_color="white", back_color="black")
    dorm.qr_image=img.save('media/qr/{}_qr.png'.format(row[1][row[1].index[2]]))
    dorm.qr_image='qr/{}_qr.png'.format(row[1][row[1].index[2]])
    dorm.save()
            
def select_file(request):
    if request.method=="POST":
        chk_file=request.POST.getlist('file[]')
        for file in chk_file:
            file_= get_object_or_404(Uploadfile, title=file)
            file_.chk=1
            file_.save()
            directory="media/file/{}.xlsx".format(file)
            df=pd.read_excel(directory, header=0)

            for row in df.iterrows():
                excel_to_db(row, file)

        return redirect("select_file")
    not_upload_files=Uploadfile.objects.filter(chk=0)
    upload_files=Uploadfile.objects.filter(chk=1)
    return render(request, 'file.html', {'upload_files':upload_files,'not_upload_files':not_upload_files})

def delete_data(request):
    if request.method=='POST':
        chk_file=request.POST.getlist('file[]')
        for file in chk_file:
            dorm1_data.objects.filter(file_name=file).delete()
            dorm2_data.objects.filter(file_name=file).delete()
            dorm3_data.objects.filter(file_name=file).delete()
            file_= get_object_or_404(Uploadfile, title=file)
            file_.chk=0
            file_.save()
    not_upload_files=Uploadfile.objects.filter(chk=0)
    upload_files=Uploadfile.objects.filter(chk=1)
    return render(request, 'file.html', {'upload_files':upload_files,'not_upload_files':not_upload_files})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def select_out(request, dorm):
    if request.method=='POST':
        student_number=request.POST['student_number']
        select=request.POST['submit']

        if(dorm=="향1"):
            dorm_= get_object_or_404(dorm1_data, student_number=student_number)
        elif(dorm=="향2"):
            dorm_= get_object_or_404(dorm2_data, student_number=student_number)
        elif(dorm=="향3"):
            dorm_= get_object_or_404(dorm3_data, student_number=student_number)

        if(select=="외출"):
            return render(request, 'outing.html',{'dorm_data':dorm_})
        else:
            return render(request, 'overnight.html',{'dorm_data':dorm_})