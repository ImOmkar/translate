from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('devToModi/clearcache/', include('clearcache.urls')),
    path('devToModi/', admin.site.urls),
    path('', include('modi.urls')),

    #pwabuilder.js link
    path('pwabuilder-sw.js', TemplateView.as_view(template_name="pwabuilder-sw.js", content_type="application/javascript"), name="pwabuilder-sw.js"),
    path('offline.html', TemplateView.as_view(template_name="translate/offline.html", content_type="application/javascript"), name="offline.html"),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "modi.views.error_404_view"