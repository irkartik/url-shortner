"""urlshortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from shortner.views import LinkCreate
from shortner.views import LinkShow
from shortner.views import RedirectToLongURL

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', LinkCreate.as_view(), name='home'),
	url(r'^link/(?P<pk>\d+)$', LinkShow, name='link_show'),
	url(r'^r/(?P<short_url>\w+)$', RedirectToLongURL, name='redirect_short_url'),
]


# from django.conf.urls import patterns, include, url
# from django.contrib import admin
# from shorturls.views import LinkCreate
# from shorturls.views import LinkShow
# from shorturls.views import RedirectToLongURL

# urlpatterns = patterns('',
# 	url(r'^$', LinkCreate.as_view(), name='home'),
# 	url(r'^link/(?P<pk>\d+)$', LinkShow.as_view(), name='link_show'),
# 	url(r'^r/(?P<short_url>\w+)$', RedirectToLongURL.as_view(), name='redirect_short_url'),
# )