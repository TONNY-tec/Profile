from django.urls import path
from django.contrib.auth import views as auth_views
from personal import views
# from users import views as user_views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name= 'about'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('succesful/', views.succesful, name='succesful'),
]