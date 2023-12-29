from django.urls import path
from .views import *


urlpatterns = [
    path('',home),
    path('home',handlingFile.as_view())
     
    
]
