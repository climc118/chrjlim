from django.conf.urls import url
from django.urls import path

from cavern.views import JanuaryCavernView

app_name = "cavern"
urlpatterns = [
    url('january_entry', JanuaryCavernView.as_view(), name="january_cavern_view")
]
