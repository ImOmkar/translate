from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('devToModi/', admin.site.urls),
    path('', include('modi.urls')),

    
] 

handler404 = "modi.views.error_404_view"