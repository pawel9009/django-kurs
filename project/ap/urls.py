from django.urls import path
from ap import views

urlpatterns = [
    path('', views.users, name='users' )
]
