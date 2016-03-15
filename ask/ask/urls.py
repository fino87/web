from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', include(login.site.urls)),
    url(r'^signup/', include(signup.site.urls)),
    url(r'^question/\d+', 'test', name='question',)
    url(r'^ask/', include(ask.site.urls)),
    url(r'^popular/', include(popular.site.urls)),
    url(r'^new/', include(new.site.urls))
)
