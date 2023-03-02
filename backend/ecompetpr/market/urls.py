from django.urls import path
from market.views.auth import AuthView, hello
from django.conf.urls import url
from django.urls import path,include



urlpatterns = [
    path('userlogin', AuthView.as_view()),
    path('hello', hello),
]
