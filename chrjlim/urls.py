from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cavern/', include('cavern.urls')),
    path('surface/', include('surface.urls')),
    path('', RedirectView.as_view(url='surface/home'))
]
