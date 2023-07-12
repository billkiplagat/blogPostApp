from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post


@api_view(['GET'])
def index(request):
    return Response({"Success": "Setup was a Success"})


@api_view(['GET'])
def GetAllPosts(request):
    """ QuerySet is a collection of database objects obtained from a model's database
    table or a result of a database query """
    get_posts = Post.objects.all()
    return Response(get_posts)
