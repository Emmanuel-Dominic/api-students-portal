from rest_framework import serializers
from .models import Student
# from .serializers import StudentSerializer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    # @classmethod
    # def mutate(cls, root, info, **kwargs):  # create
    #     serializer = StudentSerializer(data=kwargs)
    #     if serializer.is_valid():
    #         obj = serializer.save()
    #         msg = 'success'
    #     else:
    #         msg = serializer.errors
    #         obj = None
    #         print(msg)
    #     return cls(student=obj, message=msg, status=200)

    # @classmethod
    # def mutate(cls, root, info, pk, **kwargs):  # update
    #     sub = StudentModel.objects.get(pk=pk)
    #     serializer = StudentSerializer(sub, data=kwargs, partial=True)
    #     if serializer.is_valid():
    #         obj = serializer.save()
    #         msg = 'success'
    #     else:
    #         msg = serializer.errors
    #         obj = None
    #         print(msg)
    #     return cls(subject=obj, message=msg, status=200)
