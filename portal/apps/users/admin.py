from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from .models import Student


# Register your models here.
class StudentAdminModel(admin.ModelAdmin):
    # models = Student
    list_display = (
        "email",
        "username",
        "gender",
        "password",
        "is_active"
    )
    search_fields = (
        "email",
        "username",
    )
    readonly_fields = (
        "id",
        "password",
    )


admin.site.register(Student, StudentAdminModel)
# admin.site.register(Group, GroupAdmin)
admin.site.register(Permission)
admin.site.register(LogEntry)
admin.site.register(ContentType)
admin.site.register(Session)
