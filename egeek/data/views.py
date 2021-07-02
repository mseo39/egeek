from django.shortcuts import render, redirect
from .forms import uploadfile_form
import pandas as pd
from .models import Uploadfile

# Create your views here.

def data(request):
    return render(request, 'main.html')

def select_file(request):
    if request.method=="POST":
        form=uploadfile_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("select_file")

    file_form=uploadfile_form()
    return render(request, 'main.html', {'file_form':file_form})

