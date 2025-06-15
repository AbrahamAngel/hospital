from django.urls import path
from authentication.views import login_user_view, logout_user, register_user_view, doctor_dashboard, patient_dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_user_view, name='register'),
    path('login/', login_user_view, name='login'),
    path('logout/', logout_user, name='logout'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor-dashboard'),
    path('patient/dashboard/', patient_dashboard, name='patient-dashboard')
]