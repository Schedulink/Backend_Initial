from django.urls import path
from .import views

urlpatterns=[
    # re_path(r'^Admin$',views.AdminApi),
    # re_path(r'^Admin/([0-9])+$',views.AdminApi)
    # path('admin-list/',views.showall,name='admin-list'),
    path('department/',views.showalldep,name='dept-list'),
    path('degreeprogram/',views.showalldegpgm,name='Degpgm-list'),
    path('Semester/',views.showallsem,name='Semester-list'),
    path('Subject/',views.showallsem,name='Subject-list'),
    path('Faculty/',views.showallsem,name='Faculty-list'),
    path('overall-show/',views.overallshow,name='overall-list'),
     path('For-pas/',views.forgetpass,name='For_pass'),
    # path('overall-create/',views.overallcreate,name='overall-create'),
    # path('admin-create/',views.Admincreate)
    
] 