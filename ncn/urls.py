"""ncn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.static import serve as media_serve

from ncn.components.view_root import mock_api, resume

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", resume),
    path("mock/", mock_api),
    path("user/", include("user.urls")),
    path("notes/", include("notes.urls")),
    path("news/", include("news.urls")),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns.append(path(
        'media/<path:path>',
        media_serve,
        {"document_root": settings.MEDIA_ROOT}
    ))

print(f'\nDEBUG: {settings.DEBUG} \n')

# import pprint 
# pprint.pprint(urlpatterns)
