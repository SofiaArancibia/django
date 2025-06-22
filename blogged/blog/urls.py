from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.detail, name='detail'),  # URL pattern for post detail view
    path('', views.index, name='index')
]