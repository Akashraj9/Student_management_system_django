
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.import views,Hod_views,Staff_views,Students_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    # login path
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    # This is Hod panel url
    path('Hod/Home',Hod_views.HOME,name='hod_home'),

]

