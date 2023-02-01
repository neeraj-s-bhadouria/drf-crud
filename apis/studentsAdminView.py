from django.contrib import admin


class StudentsAdminView(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'standard', 'roll_number', 'is_active', 'date_created']