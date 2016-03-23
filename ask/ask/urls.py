from django.conf.urls import url
from django.conf.urls import include
#from django.contrib import admin

urlpatterns = [

    url(r'^$', include('qa.urls'), name='root'),
    url(r'^login/', include('qa.urls'), name='signin'),
    url(r'^signup/', include('qa.urls'), name='signup'),
    url(r'^question/([0-9,A-Z,a-z]{3})/',  include('qa.urls'), name='question'),
    url(r'^ask/', include('qa.urls'), name='ask'),
    url(r'^popular/', include('qa.urls'), name='popular'),
    url(r'^new/', include('qa.urls'), name='new'),
    #url(r'^admin/', admin.site.urls),
]
