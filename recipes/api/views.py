from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.api.permissions import IsAuthorOrReadOnly
from recipes.api.serializers import RecipeSerializer, CommentSerializer
from recipes.models import Recipe, Comment


class CommentCreateAPIView(generics.CreateAPIView):
    """Allow user to create a comment if they didn't yet"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        recipe = get_object_or_404(Recipe, slug = kwarg_slug)

        if recipe.comments.filter(author=request_user).exists():
            raise ValidationError("You have already creatd a comment for this recipe")

        serializer.save(author=request_user, Recipe=recipe)


class CommentLikeAPIView(APIView):
    """Allow user to add/remove a like to a recipe"""
    serializer_class = CommentSerializer
    permission_class = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of a recipe"""
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.voters.remove(user)
        comment.save

        serializer_context = {"request": request}
        serializer = self.serializer_class(recipe, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the recipe voters"""
        recipe = get_object_or_404(Recipe, pk=pk)
        user = request.user

        comment.voters.add(user)
        comment.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(recipe, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentListAPIView(generics.ListAPIView):
    """Provide the comments queryset of a specific recipe"""
    serializer_class = CommentSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Comment.objects.filter(recipe__slug=kwarg_slug).order_by("-created_at")


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for a comment to its author"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [IsAuthenticated, IsAuthorOrReadOnly]


class RecipeViewSet(viewsets.ModelViewSet):
    """Provide CRUD functionality for recipe"""
    queryset = Comment.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = RecipeSerializer
    permission_class = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)