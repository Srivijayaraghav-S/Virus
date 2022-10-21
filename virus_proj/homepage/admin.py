from django.contrib import admin
from .models import Students,Recruiters,StudentUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(StudentUser,UserAdmin)
admin.site.register(Students)
admin.site.register(Recruiters)