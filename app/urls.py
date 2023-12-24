
from django.urls import path
from app.views import Parser,AdditionalInfo

urlpatterns = [
    path('parsing-file/',Parser.as_view(),name='file_parser'),
    path('additional-info/',AdditionalInfo.as_view(),name='file_parser'),
]
