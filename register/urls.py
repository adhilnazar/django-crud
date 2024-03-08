from django.urls import path
from. import views
urlpatterns = [
    path('regi_ster',views.regi_ster,name="regi_ster"),
    path('home',views.home,name="home"),
    path('',views.log_in,name="log_in"),
    path('log_out',views.log_out,name="log_out")
]