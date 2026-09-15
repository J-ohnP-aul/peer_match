from django.urls import path
from .views import academic_profile_v, academic_profile_success_v, select_units_v

urlpatterns = [
  path("academic-profile/", academic_profile_v, name="academic_profile"),
  path("select-units/",select_units_v, name="select_units"),
  path("academic-profile/complete/",academic_profile_success_v,name="academic_profile_success"),
]