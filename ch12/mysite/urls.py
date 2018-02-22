from django.contrib import admin
from django.urls import path #알아보기

from django.conf.urls import include, url
from django.urls import include, re_path #추가

from mysite.views import HomeView

#from bookmark.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
]
