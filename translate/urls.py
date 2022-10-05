from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('devToModi/clearcache/', include('clearcache.urls')),
    path('devToModi/', admin.site.urls),
    path('', include('modi.urls')),

    #pwabuilder.js link
    path('pwabuilder-sw.js', TemplateView.as_view(template_name="pwabuilder-sw.js", content_type="application/javascript"), name="pwabuilder-sw.js"),
    path('manifest.json', TemplateView.as_view(template_name="static/manifest.json", content_type="application/javascript"), name="manifest"),

    
] 

handler404 = "modi.views.error_404_view"