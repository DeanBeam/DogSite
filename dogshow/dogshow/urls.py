"""dogshow URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from news.views import index,contacts
from DogBase.views import labrador_view, cavaliers_view,detail_view
from NewPuppies.views import weSharePuppies_view, weHadGrowth_view, photoPuppies_detailview
from PhotoBase.views import allPhotos_view
from dogshow import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^photos/$', allPhotos_view, name="photoLib"), 
    url(r'^puppies/(?P<pairLiter>\w+)/$', photoPuppies_detailview, name="puppiesShare"),
    url(r'^history/(?P<pairLiter>\w+)/$', photoPuppies_detailview, name="puppiesHistory"), 
    url(r'^contacts/$', contacts, name="contacts"),  
    url(r'^history/$', weHadGrowth_view, name="puppiesHistory"),    
    url(r'^puppies/$', weSharePuppies_view, name="puppiesShare"),
    # url(r'^cavalers/$', cavaliers_view, name="cavalers"),
    url(r'^(?P<dogtype>\w+)/$', labrador_view, name="dog"),
    url(r'^(?P<dogSlug>\w+)/$', detail_view, name="detailDog"),
    url(r'^$', index, name="index"),
]
if settings.DEBUG:
 urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
