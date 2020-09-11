from django.conf.urls import url, include
from . import views

app_name="medicinas_app"

urlpatterns = [

	url('aceites', views.AceitesView.as_view(), name="aceites"),
	url('parches', views.ParchesView.as_view(), name="parches"),
	url('cremas', views.CremasView.as_view(), name="cremas"),
	url('pastillas', views.PastillasView.as_view(), name="pastillas"),
	url('plantas', views.PlantasView.as_view(), name="plantas"),
	url('cuidado', views.CuidadoView.as_view(), name="cuidado"),
	url(r'^buscar/', views.buscar, name='buscar'),
]