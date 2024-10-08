from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
# for function based apiview 
from rest_framework.decorators import api_view
# for class based apiview
from rest_framework.views import APIView

# for generic apiview 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

# viewsets view
from rest_framework import viewsets
# Create your views here.

# function based apiview 
@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        # pk = request.data.get(id)
        if pk is not None:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors)

    if request.method =='DELETE':
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg': 'Data Deleted'})
    
# class based apiview 
class StudentAPI(APIView):
    def get(self, request,pk=None, format=None):
        if pk is not None:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors)
    
    def patch(self, request, pk, format=None):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors)
    
    def delete(self, request, pk, format=None):
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg': 'Data Deleted'})
 
# generic api view 
class GPStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   
class PDStudentAPI(GenericAPIView,UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# viewsets class api
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print(self.basename)
        print(self.suffix)
        print(self.name)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        if pk is not None:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg': 'Data Deleted'})


#ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

#ReadOnlyModelViewSet
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer





