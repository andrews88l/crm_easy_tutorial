"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from marketing.views import HomePage
from subscribers import views as subscriber_views

urlpatterns = patterns('', 

	# Marketing Pages
	url(r'^$', HomePage.as_view(), name="home"),

	# Subscriber-related URLs
	url(r'^signup/$', 'crmapp.subscribers.views.subscriber_new', name = 'sub_new'),

	# Admin URL
	url(r'^admin/', include(admin.site.urls)),

	# Login/Logout URLs

	# Account-related URLs

	# Contact-related URLs

	# Communication-related URLs

)