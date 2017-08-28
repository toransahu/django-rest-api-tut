from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

from snippets.serializers import UserSerializer
from django.contrib.auth.models import User


# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or crete a new snippet.

    REST framework provides a set of already mixed-in generic views.
    """
    
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    """
    [+] Associating Snippets with users.
        The way we deal with that is
        by overriding a .perform_create() method on our snippet views,
        that allows us to modify how the instance save is managed,
        and handle any information that is implicit in the incoming request or requested URL.

        The create() method of our serializer will now be passed an additional 'owner' field,
        along with the validated data from the request.
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.

    REST framework provides a set of already mixed-in generic views
    """
    
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(genericx.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
