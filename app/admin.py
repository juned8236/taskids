from django.contrib import admin
from app.models import TestTable,UserProfileInfo,User
# Register your models here.



class TestAdmin(admin.ModelAdmin):
    class Meta:
        model = TestTable
        fieldsets = '__all__'
admin.site.register(TestTable,TestAdmin)

admin.site.register(UserProfileInfo)