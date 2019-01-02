from django.conf.urls import url
from django.urls import path

from surface.views import SurfaceHomeView, ViewSurface

app_name = "surface"
urlpatterns = [
    url('home', SurfaceHomeView.as_view(), name="surface_home_view")
]
