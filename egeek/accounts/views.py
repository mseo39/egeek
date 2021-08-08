from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from data.models import manager

# Create your views here.

def signup(request):
    if request.method == 'POST': #정보를 전달하는 방식
        username_list=request.POST.getlist('username[]')
        password_list=request.POST.getlist('password[]')
        manager_=manager()
        print(username_list)
        print(password_list)
        #유저를 만들어 줌
        for i, username in enumerate(username_list):
            print(username)
            print(password_list[i])
            User.objects.create_user(username=username, password=password_list[i])
            manager.objects.get(username=username).delete()
        return redirect('manager')
    return render(request, 'signup.html', {'username':'', 'chk':'중복확인', 'able':'disabled'})

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
            return render(request, 'login.html', {'error': '아이디나 비밀번호가 틀립니다'})
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
        if(username==''):
            return render(request, 'signup.html', {'error': 'username이 비어있습니다', 'username':'', 'chk':'중복확인', 'able':'disabled'}) 
        for f in User.objects.all():
            if(f.username == username):
                return render(request, 'signup.html', {'error': 'username이 중복됩니다', 'username':'', 'chk':'중복확인', 'able':'disabled'})
        return render(request, 'signup.html', {'username':username, 'chk':'사용가능', 'able':''})
    else:
        return redirect('signup')

def signup_apply(request):
    if request.method == 'POST': #정보를 전달하는 방식
        username = request.POST['username']
        
        if request.POST['password1'] == request.POST['password2']: #비밀번호 확인
            manager_=manager()
            manager_.username=request.POST['username']
            manager_.password=request.POST['password1']
            manager_.save()
            return render(request, 'signup.html', {'success': '가입이 완료되었습니다', 'username':'', 'chk':'중복확인', 'able':'disabled'}) 
        else:
            return render(request, 'signup.html', {'error': '비밀번호가 다릅니다', 'username':username, 'chk':'중복확인', 'able':'disabled'})
    return username_chk(request)
    

def manager_(request):
    manager_=manager.objects.all()
    return render(request, 'manager.html', {'managers':manager_})