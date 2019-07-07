from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from .views import homepage, accounts, mappings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name="home"),
    path('maps/', mappings, name="maps" ),
    path('accounts/', accounts, name="accounts"),
    path('profile/', include('user_profile.urls')),
    path('staff/', include('my_staff.urls')),
    path('students/', include('students.urls')),
    path('parents/', include('parents.urls')),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
