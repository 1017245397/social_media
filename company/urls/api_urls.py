from company.views.api_views import CompanyViewSet, ContactCompanyViewSet, CategoryCompanyViewSet, \
    GaleryCompanyViewSet,CommentCompanyViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('list', CompanyViewSet)
router.register('contact', ContactCompanyViewSet)
router.register('categories', CategoryCompanyViewSet)
router.register('galery', GaleryCompanyViewSet)
router.register('comment', CommentCompanyViewSet)


urlpatterns = router.urls 

