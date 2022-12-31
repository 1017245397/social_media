from company.views.api_views import CompanyViewSet, ContactCompanyViewSet, CategoryCompanyViewSet, \
    GaleryCompanyViewSet,CommentCompanyViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router: DefaultRouter = DefaultRouter()
router.register('list', CompanyViewSet)
router.register('contact', ContactCompanyViewSet)
router.register('categories', CategoryCompanyViewSet)
router.register('galery', GaleryCompanyViewSet)
router.register('comment', CommentCompanyViewSet)


urlpatterns = router.urls 

