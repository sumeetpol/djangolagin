from django.contrib import admin

# Register your models here.
from . models import mainsignup,Signup,Multiimage,Fav_list

admin.site.register(mainsignup)
admin.site.register(Signup)
admin.site.register(Multiimage)
admin.site.register(Fav_list)