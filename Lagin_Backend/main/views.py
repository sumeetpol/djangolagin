from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import mainsignup,Signup,Fav_list
from .serializers import MainsignupSerializer,SignupSerializer,FavSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'POST','PUT','DELETE'])
def main_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        sig1=mainsignup.objects.all()
        sig2=MainsignupSerializer(sig1, many=True)
        return Response(sig2.data)

    elif request.method == 'POST':
        serializer = MainsignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        serializer = MainsignupSerializer(mainsignup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mainsignup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def Main_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = mainsignup.objects.get(pk=pk)
    except mainsignup.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MainsignupSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MainsignupSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST'])
@csrf_exempt
def Main_image(request, pk):
    try:
        snippet = mainsignup.objects.get(pk=pk)
    except mainsignup.DoesNotExist:

        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = MainsignupSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        serializer = MainsignupSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = mainsignup.objects.all()
    serializer_class = MainsignupSerializer
    
@api_view(['GET', 'POST','PUT','DELETE'])
def signup_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        sig1=Signup.objects.all()
        sig2=SignupSerializer(sig1, many=True)
        return Response(sig2.data)

    elif request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        serializer = SignupSerializer(Signup(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Signup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class SignupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer


@csrf_exempt
def Signup_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Signup.objects.get(pk=pk)
    except Signup.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SignupSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SignupSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def Fav_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Fav_list.objects.get(pk=pk)
    except Fav_list.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FavSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FavSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

class FavViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Fav_list.objects.all()
    serializer_class = FavSerializer

@api_view(['GET', 'POST','PUT','DELETE'])
def fav_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        sig1=Fav_list.objects.all()
        sig2=FavSerializer(sig1, many=True)
        return Response(sig2.data)

    elif request.method == 'POST':
        serializer = FavSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        serializer = FavSerializer(Fav_list(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Fav_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)