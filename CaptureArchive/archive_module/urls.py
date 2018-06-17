from django.conf.urls import url
from . import views

urlpatterns = [
    url( '^send_capture_content', views.send_capture_content, name='send_capture_content' )
]
