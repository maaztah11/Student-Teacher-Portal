from django.urls import path
from main import views
from stdportal import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='index'),
    path('delete/<int:id>/', views.delete, name='delete-student'),
    path('edit/<int:id>/', views.edit, name='edit-student')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)