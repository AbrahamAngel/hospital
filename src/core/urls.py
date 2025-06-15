from django.urls import path
from core.views import login_page_view

urlpatterns = [
    path('login-page/', login_page_view, name='login-page'),

]