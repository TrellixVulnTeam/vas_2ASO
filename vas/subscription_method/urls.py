from django.urls import path,re_path
from . import views

urlpatterns = [
    path('/data/', views.data),
    re_path('', views.detail),

]
