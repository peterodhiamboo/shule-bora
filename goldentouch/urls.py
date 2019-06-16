from django.contrib import admin
from django.urls import path, include
from .views import homepage, accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name="home"),
    path('accounts/', accounts, name="accounts"),
    path('profile/', include('user_profile.urls')),
]
