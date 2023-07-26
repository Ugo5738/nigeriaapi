from django.urls import include, path
from rest_framework.routers import DefaultRouter

from locations.views import LocationView  # , LocationViewSet

# router = DefaultRouter()
# router.register(r'locations', LocationViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('locations/', LocationView.as_view(), name='all_locations'),
    path('locations/<str:state>/', LocationView.as_view(), name='state_locations'),
    path('locations/<str:state>/<str:local_govt>/', LocationView.as_view(), name='localgovt_locations'),
]
