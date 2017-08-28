from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics



# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or crete a new snippet.

    REST framework provides a set of already mixed-in generic views.
    """
    
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.

    REST framework provides a set of already mixed-in generic views
    """
    
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    
