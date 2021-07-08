from django.shortcuts import get_object_or_404, render, redirect
from .forms import uploadfile_form
import pandas as pd
from .models import Uploadfile, dorm1_data, dorm2_data,dorm3_data
import qrcode

def main(request):
    return render(request, 'home.html')

def detail(request,dorm, student_number):
    print(dorm)
    print(student_number)
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
            directory="media/file/{}.xlsx".format(file)
            df=pd.read_excel(directory, header=0)

            for row in df.iterrows():
                excel_to_db(row)

        return redirect("select_file")
    files=Uploadfile.objects.all()
    return render(request, 'file.html', {'files':files})

