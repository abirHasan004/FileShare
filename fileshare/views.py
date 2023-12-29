import json
from django.shortcuts import render
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
 
# Create your views here.
class handlingFile(APIView):
    def post(self,request):
        data=request.data
        serializer=FileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'status':200,
                'message':'your are now ok',
                'data':serializer.data,
               
            })
        return Response(status=300)
    
   
def home(request):
    print(request)
    return render(request,'index.html')