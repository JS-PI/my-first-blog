from django.contrib import admin
from django.urls import path #알아보기

from django.conf.urls import url
from django.urls import include, re_path

#from bookmark.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.urls)),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    #url(r'^bookmark/', include('bookmark.urls')),
    #url(r'^blog/', include('blog.urls')),
]
