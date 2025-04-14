from django.http import HttpResponse
from django.urls import path,include
from . import views

urlpatterns=[

    path("",views.home,name="home"),
    path("login_redirect",views.login_redirect,name="login_redirect"),
    path("ctoauthsignup",views.ctoAuthSignup,name="ctoAuthSignup"),
    path("ctoauthlogin",views.ctoAuthLogin,name="ctoAuthLogin"),
    path("ctopage",views.ctopage,name="ctopage"),
    path("ctospm",views.cto_spm,name="cto_spm"),
    path("spm_auth_login",views.spmAuthLogin,name="spmAuthLogin"),
    path("pm_auth_login",views.pmAuthLogin,name="pmAuthLogin"),
    path("intern_auth_login",views.internAuthLogin,name="internAuthLogin"),
    path("uiux_auth_login",views.uiuxAuthLogin,name="uiuxAuthLogin"),
    path("devops_auth_login",views.devopsAuthLogin,name="devopsAuthLogin"),
    path("network_auth_login",views.networkAuthLogin,name="networkAuthLogin"),
    path("seniordev_auth_login",views.seniordevAuthLogin,name="seniordevAuthLogin")
]