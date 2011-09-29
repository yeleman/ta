from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples: 
    # url(r'^download_m/', include('download_m.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r"^$", "ylm_download.views.home", name="home"),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
