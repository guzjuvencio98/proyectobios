from django.conf.urls import url, include
from . import views

app_name="home_app"

urlpatterns = [
	url('index', views.IndexView.as_view(), name="index")
]