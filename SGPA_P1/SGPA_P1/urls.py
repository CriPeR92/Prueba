from django.contrib import admin
from django.conf.urls import patterns, include, url
from login.views import *
admin.autodiscover()
 
 
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Administrar/$', home),
    url(r'^Administrar/Administrar_Usuarios/', modulo2),
    
   # url(r'^Administrar_Usuarios', modulo2),
    
    
    #url(r'^$', 'usuario_datos.views.home', name='home'),
    #url(r'^crear/', 'usuario_datos.views.crear', name='crear'),

)
