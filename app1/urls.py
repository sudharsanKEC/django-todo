from django.http import HttpResponse
from django.urls import path,include
from . import views

urlpatterns=[
    path("ctoauthsignup",views.ctoAuthSignup,name="ctoAuthSignup"),
    path("ctoauthlogin",views.ctoAuthLogin,name="ctoAuthLogin"),
    path("ctopage",views.ctopage,name="ctopage")
]