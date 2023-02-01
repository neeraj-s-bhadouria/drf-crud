from django.contrib import admin
from .models import Students
from .studentsAdminView import StudentsAdminView


admin.site.register(Students, StudentsAdminView)
