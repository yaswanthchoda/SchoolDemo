from django.contrib import admin
from django.contrib.auth import get_user_model
from schapp.models import Student

# Register your models here.

# class UserAdmin(admin.ModelAdmin):
# 	last_display = ['id', 'username']
# 	class Meta:
# 		model = User

# class SchoolAdmin(admin.ModelAdmin):
# 	list_display = ['username', 'email']

# 	class Meta:
# 		model = School

# class StudentAdmin(admin.ModelAdmin):
# 	list_display = ['age', 'id']

# 	class Meta:
# 		model = Student

# admin.site.register(School,   SchoolAdmin)
# admin.site.register(Student, StudentAdmin)

