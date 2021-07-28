"""egeek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import data.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', data.views.main, name="main"),
    path('detail/<str:dorm>/<int:student_number>',data.views.detail, name="detail"),
    path('detail/<str:dorm>/select_out',data.views.select_out, name="select_out"),
    path('upload_file', data.views.upload_file, name="upload_file"),
    path('select_file', data.views.select_file, name="select_file"),
    path('delete_data', data.views.delete_data, name="delete_data"),
    path('accounts/',include('accounts.urls')),
    path('manager/', accounts.views.manager_, name="manager"),
    path('overnight',data.views.overnight, name="overnight")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)