from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from .views import homepage, accounts, mappings, validate_upi
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maps/', mappings, name="maps" ),
    path('ajax/validate_upi/', validate_upi, name="validate_upi"),
    path('accounts/', accounts, name="accounts"),
    path('', include('user_profile.urls')),
    path('staff/', include('my_staff.urls')),
    path('students/', include('students.urls')),
    path('parents/', include('parents.urls')),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
