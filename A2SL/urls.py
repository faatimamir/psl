"""A2SL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.urls import path, include
from A2SL import views


# urlpatterns = [
#     #path('video_feed', views.video_feed, name='video_feed'),
#     path('webcam_feed', views.webcam_feed, name='webcam_feed'),
#     path('admin/', admin.site.urls),
#     path('about/',views.about_view,name='about'),
#     path('contact/',views.contact_view,name='contact'),
#     path('login/',views.login_view,name='login'),
#     path('logout/',views.logout_view,name='logout'),
#     path('signup/',views.signup_view,name='signup'),
#     path('animation/',views.animation_view,name='animation'),
#     path('sltotext/', views.sltotext_view ,name='sltotext'),
#     # path('', views.opencam, name='opencam'),
#     path('',views.home_view,name='home'),
     
# ]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    #path('video_feed', views.video_feed, name='video_feed'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    path('admin/', admin.site.urls),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact'),
    
    
    
    path('animation/',views.animation_view,name='animation'),
    path('sltotext/', views.sltotext_view ,name='sltotext'),
    # path('', views.opencam, name='opencam'),
    path('',views.home_view,name='home'),
    path('webcam_feed/<str:mode>/', views.webcam_feed, name='webcam_feed_mode'),
     
]