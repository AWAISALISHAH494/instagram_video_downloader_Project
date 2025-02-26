from django.urls import path
from . import views
from django.urls import path
from .views import index, download_content
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download_content, name='download_content'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)