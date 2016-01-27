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

from accounts.urls import account_urls
from contacts.urls import contact_urls

admin.autodiscover()

from marketing.views import HomePage
from subscribers import views as subscriber_views
from accounts.views import AccountList

urlpatterns = patterns('', 

	# Marketing Pages
	url(r'^$', HomePage.as_view(), name="home"),

	# Subscriber-related URLs
	url(r'^signup/$', 'crmapp.subscribers.views.subscriber_new', name = 'sub_new'),

	# Admin URL
	url(r'^admin/', include(admin.site.urls)),

	# Login/Logout URLs
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'login.html'}),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/login/'}),

	# Account-related URLs
	url(r'^account/new/$', 'crmapp.accounts.views.account_cru', name='account_new'),
	url(r'^account/list/$', AccountList.as_view(), name='account_list'),
	url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),

	# Contact-related URLs
	url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),
	url(r'^contact/new/$', 'crmapp.contacts.views.contact_cru', name='contact_new'),

	# Communication-related URLs

)