from django.contrib import admin
from django.conf import settings
from django.urls import path, include
# from . views import homepage, accounts, mappings, validate_upi, login, validate_amount
from . import views
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maps/', views.mappings, name="maps" ),
    path('ajax/validate_upi/', views.validate_upi, name="validate_upi"),
    path('ajax/validate_amount_and_make_payments/', views.validate_amount, name="validate_amount"),
    path('accounts/', views.accounts, name="accounts"),
    path('', include('user_profile.urls')),
    path('staff/', include('my_staff.urls')),
    path('students/', include('students.urls')),
    path('parents/', include('parents.urls')),
    path('login/', views.login, name="login"),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls))       
    ] + urlpatterns
