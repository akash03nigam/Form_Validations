from django.contrib import admin
from Forms_app.models import StudentRegister
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['Name','Email']

admin.site.register(StudentRegister,StudentAdmin) 