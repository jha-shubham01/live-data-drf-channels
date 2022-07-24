from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()


def index(request):
    return render(request, "demo/index.html")
