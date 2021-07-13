from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST': #정보를 전달하는 방식
        if request.POST['password1'] == request.POST['password2']: #비밀번호 확인
            #유저를 만들어 줌
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            #로그인하는 함수
            auth.login(request, user)
            return redirect('main') #성공하면 
    return render(request,'signup.html', {'username':' '}) #실패하면

def login(request):
    if request.method == 'POST': #정보를 전달하는 방식
        username = request.POST['username']
        password = request.POST['password']
        #회원정보가 있는지 확인
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: #있으면
            auth.login(request, user)
            return redirect('main')
        else: #없으면
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'login.html') #실패하면

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'login.html')

def username_chk(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = auth.authenticate(request, username=username)
        if user is not None: #있으면
            return render(request, 'signup.html', {'error': 'ss', 'username':''})
        else: #없으면
            return render(request, 'signup.html', {'error': 'username or password is incorrect', 'username':username})
    else:
        return redirect('signup')