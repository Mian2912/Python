from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'order','created_at']

#el serializador utiliza el modelo Post y le indicamos
# los campos que van a retornar