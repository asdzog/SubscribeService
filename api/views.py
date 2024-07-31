from rest_framework import generics, permissions
from blog.models import Article
from .serializers import UserSerializer, ArticleSerializer


class PublicArticleListView(generics.ListAPIView):
    """Представление для получения всех публичных статей."""

    queryset = Article.objects.filter(is_public=True)
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]


class ArticleListView(generics.ListCreateAPIView):
    """Представление для получения и создания статей. Только авторы могут создавать статьи."""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        """Сохраняет новую статью с текущим пользователем в качестве автора."""
        serializer.save(author=self.request.user)

    def get_queryset(self):
        """Возвращает все статьи для авторов и публичные статьи для остальных пользователей."""
        user = self.request.user
        if user.role == 'author':
            return Article.objects.all()
        return Article.objects.filter(is_public=True)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для получения, обновления и удаления статьи по ID."""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        """Определяет права доступа в зависимости от метода запроса."""
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticatedOrReadOnly()]
        return [permissions.IsAuthenticated()]

    def perform_update(self, serializer):
        """Обновляет статью, если текущий пользователь является её автором."""
        if self.request.user != serializer.instance.author:
            raise permissions.PermissionDenied('Вы не можете редактировать эту статью.')
        serializer.save()

    def perform_destroy(self, instance):
        """Удаляет статью, если текущий пользователь является её автором."""
        if self.request.user != instance.author:
            raise permissions.PermissionDenied('Вы не можете удалять эту статью.')
        instance.delete()


class UserCreateView(generics.CreateAPIView):
    """Представление для регистрации нового пользователя."""

    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
