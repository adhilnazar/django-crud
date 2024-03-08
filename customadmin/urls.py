from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('add/',views.add,name="add"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('edit/',views.edit,name="edit"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<str:id>/',views.delete,name="delete"),

]