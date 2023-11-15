from django.contrib import admin
from .models import Admin,Department,Degreeprogram,Semester,Subject,Faculty,TimetableData

# Register your models here.
admin.site.register(Admin)
admin.site.register(Department)
admin.site.register(Degreeprogram)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Faculty)
admin.site.register(TimetableData)