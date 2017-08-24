from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201) #201 for created
        """
	400 for bad request.
	The client to the server didn't follow the rules.
	"""
        return JsonResponse(serializer.errors, status=400)
		
"""
Note that because we want to be able to POST to this view from clients that wont have a CSRF token we need to mark the view as csrf_exempt. 
This isnt something that youd normally want to do, 
and REST framework views actually use more sensible behavior than this,
but it'll do for our purposes right now.
"""
@csrf_exempt
def snippet_detail(request,pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404) #page not found

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400) #bad request

    elif request.method == 'DELETE':
        snippet.delete()
        """
	The HTTP 204 No Content success status response code indicates that the request has succeed, 
	but that the client doesn't need to go away from its current page.
	"""
        return HttpResponse(status=204)
		
        
