from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('devToModi/clearcache/', include('clearcache.urls')),
    path('devToModi/', admin.site.urls),
    path('', include('modi.urls')),

    
] 

handler404 = "modi.views.error_404_view"