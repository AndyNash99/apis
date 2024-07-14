from django.urls import path
from timestamp import views

app_name='timestamp'
urlpatterns = [
    path('<str:date_string>', views.TimestampView.as_view(), name='timestamp'),
]
