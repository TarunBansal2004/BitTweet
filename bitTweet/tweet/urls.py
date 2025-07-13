from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
   path('',views.index, name='index'),
   path('timeline/' , views.timeline , name="timeline"),
   path('delete/<int:tweet_id>/', views.tweet_delete, name='tweet_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
