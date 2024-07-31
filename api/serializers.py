from rest_framework import serializers
from users.models import User
from blog.models import Article


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя."""
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Создает и возвращает нового пользователя."""
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'subscriber')
        )
        return user


class ArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели статьи."""

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'is_public', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author']
