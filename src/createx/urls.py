"""
URL configuration for createx project.

The `urlpatterns` list routes URLs to test_views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function test_views
    1. Add an import:  from my_app import test_views
    2. Add a URL to urlpatterns:  path('', test_views.home, name='home')
Class-based test_views
    1. Add an import:  from other_app.test_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('main.urls')),
]
