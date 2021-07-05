from django.contrib import admin
from data.models import Uploadfile, dorm1_data, dorm2_data, dorm3_data
# Register your models here.

admin.site.register(Uploadfile)
admin.site.register(dorm1_data)
admin.site.register(dorm2_data)
admin.site.register(dorm3_data)