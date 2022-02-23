from pyexpat import model
from django.contrib import admin

from .models import Student, Teacher


class TeachersInline(admin.TabularInline):
    model = Student.teacher.through
    extra = 0
    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [TeachersInline, ]
    exclude = ('teacher', )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [TeachersInline, ]
