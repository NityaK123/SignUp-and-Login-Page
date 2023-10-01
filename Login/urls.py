from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Account,name='sign'),
    path('Auth/',views.Auth,name='Authe'),
    path('login/',views.Login),
    path('signup',views.Signup)
]
