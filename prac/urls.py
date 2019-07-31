from django.conf.urls import url, include
from django.contrib import admin

from stats import views

from stats.api import DomainStatsResource

domain_stats_resource = DomainStatsResource()

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^index/$',views.index),
	url(r'^logout/$',views.logout),
	url(r'^get/(?P<pk>[\d]+)/$',views.get),
	url(r'^api/',include(domain_stats_resource.urls))
]
