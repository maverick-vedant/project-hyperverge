from django.urls import path
from . import views

urlpatterns = [
    path('', views.kyc_home, name='kyc_home'),
    path('form/', views.kyc_form_view, name='kyc_form'),
    path('success/', views.kyc_success, name='kyc_success'),
]
