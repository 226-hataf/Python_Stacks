
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from users import views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('users.urls'))
    path('login/', views.login_api),
    path('reg/', views.register_api)
    
]
