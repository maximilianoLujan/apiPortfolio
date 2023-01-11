from .models import blog
from rest_framework import viewsets,permissions
from .serializers import BlogSerializers

class BlogViewSet(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BlogSerializers