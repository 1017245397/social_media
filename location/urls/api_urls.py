from location.views.api_views import CountryViewSet, DeparmentViewSet, CityViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router: DefaultRouter = DefaultRouter()
router.register('country', CountryViewSet)
router.register('deparment', DeparmentViewSet)
router.register('city', CityViewSet)

urlpatterns = router.urls 