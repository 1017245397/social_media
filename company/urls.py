from company.views import CompanyViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', CompanyViewSet)

urlpatterns = router.urls 