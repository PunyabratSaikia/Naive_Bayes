from django.urls import path
from ui import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
]
