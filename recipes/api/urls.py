from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes.api import views as rv

router = DefaultRouter()
router.register(r"recipes", rv.RecipeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("recipes/<slug:slug>/comments/", rv.CommentListAPIView.as_view(), name="comment-list"),
    path("recipes/<slug:slug>/comment/", rv.CommentCreateAPIView.as_view(), name="comment-create"),
    path("comments/<int:pk>/", rv.CommentRUDAPIView.as_view(), name="comment-detail"),
    path("comments/<int:pk>/like/", rv.CommentLikeAPIView.as_view(), name="comment-like"),
]
