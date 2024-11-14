# dropbox_clone/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Dropbox Clone API. Use /api/files/ to upload or view files.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('files.urls')),
    path('', home),  # Add this line to handle the root URL
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
