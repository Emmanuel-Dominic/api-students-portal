from rest_framework import serializers
from .models import Course
from .serializers import CourseSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    # @classmethod
    # def mutate(cls, root, info, **kwargs):  # create
    #     serializer = CourseSerializer(data=kwargs)
    #     if serializer.is_valid():
    #         obj = serializer.save()
    #         msg = 'success'
    #     else:
    #         msg = serializer.errors
    #         obj = None
    #         print(msg)
    #     return cls(course=obj, message=msg, status=200)

    # @classmethod
    # def mutate(cls, root, info, pk, **kwargs):  # update
    #     sub = CourseModel.objects.get(pk=pk)
    #     serializer = CourseSerializer(sub, data=kwargs, partial=True)
    #     if serializer.is_valid():
    #         obj = serializer.save()
    #         msg = 'success'
    #     else:
    #         msg = serializer.errors
    #         obj = None
    #         print(msg)
    #     return cls(subject=obj, message=msg, status=200)
