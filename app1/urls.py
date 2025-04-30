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

    path("spm_role_creation/<int:spm_id>",views.spm_role_creation,name="spm_role_creation"),
    path("spm_assign_task_emp/<int:emp_id>",views.spm_assign_task_emp,name="spm_assign_task_emp"),

    path("emp_task_creation/<int:emp_id>",views.emp_task_creation,name="emp_task_creation"),

    path("emp_to_login",views.emp_to_login,name="emp_to_login"),
    path("emp_login/<str:role>",views.emp_login,name="emp_login"),
    path("emp_home",views.emp_home,name="emp_login")
]