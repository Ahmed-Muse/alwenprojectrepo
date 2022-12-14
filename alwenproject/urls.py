"""alwenproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#start of images 
from django.conf import settings#for uploading files
from django.conf.urls.static import static
#end of images

urlpatterns = [
    path('admin/', admin.site.urls),

    
    #path('', include('website.urls')),#this line does all the routing for the views
    path('', include('login.urls')),#point to login
    path('logistics/', include('logistics.urls')),#point to login
    path('todoapp/', include('todoapp.urls')),
]
if settings.DEBUG:#if debug which is in development stage only, then add the path below
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#this will 
