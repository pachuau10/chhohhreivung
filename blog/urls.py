from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('posts/', views.post_list, name='post_list'),  # ✅ must come BEFORE slug
    path('<slug:slug>/', views.detail, name='detail'),  # ✅ keep only once, last
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
