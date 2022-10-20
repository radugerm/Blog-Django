from django.urls import path
from . import views

app_name = 'forever'

urlpatterns = [
    path('about_me/',views.About_me,name='about_me'),
    path('contact/',views.Contact,name='contact'),
    path('pictures/',views.Pictures,name='pictures'),
    path('videos/',views.Videos,name='videos'),
    path('',views.Home,name='home'),   
    path('thank_you/',views.Thank_you,name = 'thank_you'),
]
