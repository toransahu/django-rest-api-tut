"""
Removing JSON related modules/classes

#from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer




# Create your views here.
"""
Commenting out this to use @api_view
@csrf_exempt
"""
@api_view(['GET','POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        """
        Commenting out this to use 'Response'
        return JsonResponse(serializer.data, safe=False)
        """
        return Response(serializer.data)

    elif request.method == 'POST':
        """
        Commenting out this to use 'request.data'
        data = JSONParser().parse(request)
        """
        data =request.data
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            """
            Commenting out this to use 'Response' and named status code
            return JsonResponse(serializer.data, status=201) #201 for created
            """
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        """
	    400 for bad request.
        The client to the server didn't follow the rules.
        """
        """
        Commenting out this to use 'Response' and named status code
        return JsonResponse(serializer.errors, status=400)
        """
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Note that because we want to be able to POST to this view from clients that wont have a CSRF token we need to mark the view as csrf_exempt.
This isnt something that youd normally want to do,
and REST framework views actually use more sensible behavior than this,
but it'll do for our purposes right now.
"""

"""
Commenting out to use @api_view
@csrf_exempt
"""

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        """
        Commenting out ot use 'Response'
        return HttpResponse(status=404) #page not found
        """
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        """
        Commenting out ot use 'Response'
        return JsonResponse(serializer.data)
        """"
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #bad request

    elif request.method == 'DELETE':
        snippet.delete()
        """
	The HTTP 204 No Content success status response code indicates that the request has succeed,
	but that the client doesn't need to go away from its current page.
	"""
        return Response(status=status.HTTP_204_NO_CLIENT)
