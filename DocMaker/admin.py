from django.contrib import admin
from .models import User, Subject, Experiments,UserCurrentSelectedSubjects
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Subject)
admin.site.register(Experiments)
admin.site.register(UserCurrentSelectedSubjects)
