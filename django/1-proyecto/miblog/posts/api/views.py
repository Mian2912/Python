# from rest_framework.views import APIView #esta importancion es la que no va permiter codificar el POST, DELETE, UPDATE, CREATE, WRITE
from posts.models import Post
from posts.api.serializers import PostSerializer
# Trabajar con el modelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class PostModelViewSet(ModelViewSet):
    permission_class = [IsAdminUser]
    serializer_class = PostSerializer #serializador a utilizar
    queryset = Post.objects.all()  #la query va utilizar todos los datos que vengadel modelo Post



# #trabajar con el ViewSet
# from rest_framework.viewsets import ViewSet
# # from posts.api.router import router_post
# class PostViewSet(ViewSet):
#     def list(self, request):
#         serializer = PostSerializer(Post.objects.all(), many= True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     #para crear posts con viewset se trabaja como "create"
#     def create(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def retrieve(self, request, pk:int):
#         post = PostSerializer(Post.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)


# class PostApiView(APIView):
#     def get(self, request):
#         # posts = Post.objects.all()
#         # posts = [posts.description for posts in Post.objects.all()]
#         # return Response( status=status.HTTP_200_OK, data = posts)
#         seliarizer = PostSerializer(Post.objects.all(), many = True) #devuelva el array completo de post
#         return Response(status= status.HTTP_200_OK, data=seliarizer.data)
#     def post(self, request):
#         seliarizer = PostSerializer(data=request.POST) #devuelva el array completo de post
#         seliarizer.is_valid(raise_exception=True)
#         seliarizer.save()
        #  return Response(status= status.HTTP_200_OK, data=seliarizer.data) 