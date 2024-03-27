from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_data, name='upload_data'),
]
