from django.contrib import admin
from .models import Course


# Register your models here.
class CourseAdminModel(admin.ModelAdmin):
    # models = Student
    list_display = (
        "name",
        "description",
    )
    search_fields = (
        "name",
    )
    readonly_fields = (
        "id",
    )


admin.site.register(Course, CourseAdminModel)
