from django.urls import path
from .import views


urlpatterns = [
    path('',views.login,name='login'),
    path('signup/',views.Signup,name='signup'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),

   
]
