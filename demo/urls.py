
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("post", views.PostViewSet, basename="post")

urlpatterns = [
    path("", views.index,)
]

urlpatterns += router.urls
