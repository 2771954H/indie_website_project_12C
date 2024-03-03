"""indie urls file"""

from django.urls import path
from indie import views

#working app_name-honestly would be easy to just stick to it
app_name = 'indie'

urlpatterns = [
    path('', views.index, name = 'index'),
    
    path('dev_home/', views.dev_home, name = 'dev_home'),
]

