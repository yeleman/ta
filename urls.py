from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples: 
    # url(r'^download_m/', include('download_m.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r"^$", "ylm_download.views.login", name="login"),
    url(r"^logout$", 'ylm_download.views.logout', name='logout'),
    url(r"^owner$", "ylm_download.views.owner", name="owner"),
    url(r"^add_owner$", "ylm_download.views.add_owner", name="add_owner"),
    url(r"^edit_owner$", "ylm_download.views.edit_owner", name="edit_owner"),
    url(r"^dashboard$", "ylm_download.views.dashboard", name="dashboard"),
    url(r"^gestion$", "ylm_download.views.gestion_dl", name="gestion_dl"),
    url(r"^add_dl$", "ylm_download.views.add_dl", name="add_dl"),
    url(r"^edit_dl$", "ylm_download.views.edit_dl", name="edit_dl"),
    url(r"^info_dl$", "ylm_download.views.info_dl", name="info_dl"),
    url(r"^remove_dl$", "ylm_download.views.dellete_dl", name="dellete"),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
