from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from views import HomeView, PostView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'encontroxxiv.views.home', name='home'),
    # url(r'^encontroxxiv/', include('encontroxxiv.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<pk>\d+)/$', PostView.as_view()),
)