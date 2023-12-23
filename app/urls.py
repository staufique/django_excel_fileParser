
from django.urls import path
from app.views import Parser,DataInserting

urlpatterns = [
    path('pass/',Parser.as_view(),name='file_parser'),
    path('additional/',DataInserting.as_view(),name='file_parser'),
]
