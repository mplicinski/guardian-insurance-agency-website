from django.urls import path

from .views import staff_home_view, login_view, logout_view

app_name = 'staff'
urlpatterns = [
    path('', staff_home_view, name='staff'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
