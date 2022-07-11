from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('addwidget', views.addwidget, name='addwidget'),
  path('<int:widget_id>/delete', views.deleteWidget, name='deleteWidget'),
]