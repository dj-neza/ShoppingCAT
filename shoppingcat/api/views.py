from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .serializers import MyClothingSerializer, RecommendationSerializer, InspirationSerializer
from cat.models import MyClothing, Recommendation, Inspiration

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = MyClothing.objects.all()
    serializer_class = MyClothingSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

# DOBIS INSPIRATION PREK ID-JA
@csrf_exempt
def inspirations_detail(request, pk):

	try:
		inspiration = Inspiration.objects.get(pk=pk)
	except Inspiration.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = InspirationSerializer(inspiration)
		return JsonResponse(serializer.data)

# API ZA DOBIT INSPIRATIONE
@csrf_exempt
def inspirations_user(request, username):

    if request.method == 'GET':
    	user = User.objects.get(username=username)
    	insp = Inspiration.objects.filter(user=user)
    	serializer = InspirationSerializer(insp, many=True)
    	return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# API ZA DODAJANJE INSPIRATIONA

# API GLEDE NA USERJA - PODPIRA SAMO GET
@csrf_exempt
def myclothing_user(request, username):

    if request.method == 'GET':
    	user = User.objects.get(username=username)
    	mycloth = MyClothing.objects.filter(user=user)
    	serializer = MyClothingSerializer(mycloth, many=True)
    	return JsonResponse(serializer.data, safe=False)

    """elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MyClothingSerializer(mycloth, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mycloth.delete()
        return HttpResponse(status=204)"""

# API ZA POSAMICNO OBLEKO - NE DELA SE ...
@csrf_exempt
def myclothing_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """	

    try:
        mycloth = MyClothing.objects.get(pk=pk)
    except MyClothing.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MyClothingSerializer(mycloth)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MyClothingSerializer(mycloth, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mycloth.delete()
        return HttpResponse(status=204)