from django.urls import path
from .views import *

app_name = 'authentication'
urlpatterns = [
    path('register/', Register, name='Register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forget_pass/', forget_pass),
    path('reset_pass/',reset_pass),
    path('view_all/',view_all)
]
