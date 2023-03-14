from django.urls import path
from .import views


urlpatterns = [
    
    path('',views.View),
    path('register/',views.Reg_user),
    path('login/',views.login_user),
    
        

]
