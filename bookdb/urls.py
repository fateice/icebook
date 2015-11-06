from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookdb.views.home', name='home'),
    # url(r'^bookdb/', include('bookdb.bookdb.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'data.views.index'),
    url(r'^add/','data.views.add'),
    url(r'^add_author/','data.views.add_author'), 
    url(r'^searchbook/','data.views.searchbook'),
    url(r'^searchauthor/','data.views.searchauthor'),
    url(r'^allbook/','data.views.allbook'),
    url(r'^update/','data.views.update'),
    url(r'^delete/','data.views.delete'),
    url(r'^detail/','data.views.detail'),
    url(r'^success/','data.views.add_success'),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':settings.STATIC_ROOT }),
)
