from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def index(request):
    return Response({"Success": "Setup was a Success"})


@api_view(['GET'])
def GetAllPosts(request):
    """ QuerySet is a collection of database objects obtained from a model's database
    table or a result of a database query """
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True)  # many=True mean we are passing a list of objects not 1 item
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def CreatePost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The post was created"}, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def DeletePost(request):
    # getting id from user
    post_id = request.data.get('post_id')
    try:
        # Checking if id exist in DB
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"Success": "The post was successfully deleted"}, status=200)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist in Database"}, status=404)


@api_view(['GET'])
def GetPost(request):
    # getting id from user
    post_id = request.data.get('post_id')
    try:
        # Checking if id exist in DB
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist in Database"}, status=404)


@api_view(['PUT'])
def UpdatePost(request):
    post_id = request.data.get('post_id')
    new_title = request.data.get('new_title')
    new_content = request.data.get('new_content')

    try:
        post = Post.objects.get(id=post_id)
        if new_title:
            post.title = new_title
        if new_content:
            post.content = new_content
        post.save()
        return Response({"Success": "The post was successfully updated"}, status=200)

    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist in Database"}, status=404)
