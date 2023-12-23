from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from app.models import File
import openpyxl
from django.http import HttpResponse
from .serializers import FileSerializer,AdditionalSerializer

class Parser(APIView):

    def post(self,request):
        
        data = request.FILES['file']

        workbook = openpyxl.load_workbook(data)
        print(workbook)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            name,age,roll_no,mobile,email,city,state=row
            data1=File(name=name,age=age,roll_no=roll_no,mobile_no=mobile,email=email,city=city,state=state)
            data1.save()
        
        return HttpResponse("ok")
    
class DataInserting(APIView):
    def post(self,request):
        serializer = FileSerializer(data=request.data)
        serializer2 = AdditionalSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save()
                return HttpResponse("inserted",status=status.HTTP_201_CREATED)
            return HttpResponse("inserted",status=status.HTTP_201_CREATED)
        return HttpResponse("no")
