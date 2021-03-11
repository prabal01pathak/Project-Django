from django.urls import path
from .views import sign_up_view,home_view,log_in_view

appname = 'signUp'
urlpatterns = [
    path('sign_up',sign_up_view,name = 'sign-Up'),
    path('',home_view,name = 'home-view'),
    path('log_in',log_in_view,name = 'log_in')
]