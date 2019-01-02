from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cavern/', include('cavern.urls')),
    path('surface/', include('surface.urls'))
]
