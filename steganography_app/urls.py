from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('encryption', views.encryption_view, name='encryption'),
    path('decryption', views.decryption_view, name='decryption'),
    # path('login/', views.login_view, name='login'),

]
