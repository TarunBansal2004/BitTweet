from . import views
from django.urls import path

urlpatterns = [
   path('',views.index, name='index'),
   path('other/' , views.other , name="other"),
   path('timeline/' , views.timeline , name="timeline"),
]
