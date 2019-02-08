from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^politics/', include('politics.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^profile/', include('userprofile.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()