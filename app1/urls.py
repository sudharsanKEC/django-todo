from django.http import HttpResponse
from django.urls import path,include
from . import views

urlpatterns=[

    # common pages
    path("",views.home,name="home"),
    path("login_redirect",views.login_redirect,name="login_redirect"),

    # cto related pages
    path("ctoauthsignup",views.ctoAuthSignup,name="ctoAuthSignup"),
    path("ctoauthlogin",views.ctoAuthLogin,name="ctoAuthLogin"),
    path("ctopage",views.ctopage,name="ctopage"),

    # spm related pages
    path("ctospm/<int:spm_id>/",views.cto_spm,name="cto_spm"),
    path("delete_task/<int:t_id>",views.delete_task,name="delete_task"),
    path("spm_auth_login",views.spmAuthLogin,name="spmAuthLogin"),
    path("spm_dashboard/<str:name>/<int:id>",views.spm_dashboard,name="spm_dashboard"),
    path("spm_task_toggle/<int:task_id>",views.toggle_spm_task_checkbox,name="toggle_spm_task_checkbox"),

    path("intern_auth_login",views.internAuthLogin,name="internAuthLogin"),
    path("uiux_auth_login",views.uiuxAuthLogin,name="uiuxAuthLogin"),
    path("devops_auth_login",views.devopsAuthLogin,name="devopsAuthLogin"),
    path("network_auth_login",views.networkAuthLogin,name="networkAuthLogin"),
    path("seniordev_auth_login",views.seniordevAuthLogin,name="seniordevAuthLogin")
]