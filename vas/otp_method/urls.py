from django.urls import path,re_path
from . import views

urlpatterns = [
    path('/data/', views.data),
    path('/pushotp/', views.push_otp),
    path('/chargeotp/', views.charge_otp),
    re_path('', views.detail),
]
