from django.contrib import admin
from hack.models import AddClass
from hack.models import StudentInfo

# Register your models here.

class AddClassAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['class_name']})
    ]

class StudentInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['number']}),
        (None, {'fields': ['email']})
    ]

admin.site.register(AddClass, AddClassAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
