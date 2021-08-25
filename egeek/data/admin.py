from django.contrib import admin
from data.models import Uploadfile, dorm1_data, dorm2_data, dorm3_data, manager, old_dorm1_data,old_dorm2_data,old_dorm3_data,global_dorm_data, overnight_stay, overnight_list, qrfile
# Register your models here.

admin.site.register(Uploadfile)
admin.site.register(dorm1_data)
admin.site.register(dorm2_data)
admin.site.register(dorm3_data)
admin.site.register(old_dorm1_data)
admin.site.register(old_dorm2_data)
admin.site.register(old_dorm3_data)
admin.site.register(global_dorm_data)
admin.site.register(manager)
admin.site.register(overnight_stay)
admin.site.register(overnight_list)
admin.site.register(qrfile)