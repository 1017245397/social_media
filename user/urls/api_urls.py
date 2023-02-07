from user.views.api_views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router: DefaultRouter = DefaultRouter()
router.register('user', UserViewSet)
router.register('profile-user', ProfileUserViewSet)
urlpatterns = router.urls 