from django.urls import path, re_path
from . import views

app_name = 'photos'
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    re_path(r'^upload/$', views.create, name='create'),
    path('', views.index, name = 'list'),
    path('delete/', views.delete, name='delete'),

]