
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("post", views.PostViewSet, basename="post")

urlpatterns = router.urls