"""OER_C URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from OxE.views import homepage_view, domain_view, about_view , vix_view , demo_view , player_image_view , module_cards_detail_view, domain_sub_view, cma_page
urlpatterns = [
    
path('', homepage_view , name= "home"),
path('playerImage', player_image_view , name="player_image_view"),
re_path('domain$', domain_view ),
path('about', about_view),
path('cscroll' , demo_view),
path('module_details' , module_cards_detail_view),
path('admin/', admin.site.urls),
re_path('domain/(?P<domain_name>\w+)$', domain_sub_view,name="domain_sub_view"),
path('cmspage', cma_page),

]
