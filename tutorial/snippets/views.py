from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

from snippets.serializers import UserSerializer
from django.contrib.auth.models import User

from rest_framework import permissions

from snippets.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers



# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or crete a new snippet.

    REST framework provides a set of already mixed-in generic views.
    """
    
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    """
    To make sure that only authenticated users are able to
    create, update and delete code snippets.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

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

    """
    To make sure that only authenticated users are able to
    create, update and delete code snippets.
    
    To maintane 'Object level permissions'.
    To make sure that only the user that
    created a code snippet is able to update or delete it.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""
1. Fucntion-based view for API root URL, using @api_view.
2. Using 'reverse' to return fully-qualified URLs.
"""

@api_view(['GET'])
def api_root(request, format=None):
    """
    [+]django_framework.reverse()
    1. Signature: reverse(viewname, *args, **kwargs)
    2. Has the same behavior as django.urls.reverse,
    except that it returns a fully qualified URL,
    using the request to determine the host and port.
    3. 'user-list' and 'snippet-list' are URL name in snippets/url.py
    """
    return Response(
        {
            'users': reverse('user-list', request=request, format=format),
            'snippets': reverse('snippet-list', request=request, format=format)
        }
    )
                             
"""
1. Class-based view for Highlighted code snippet end-point, and will create our custom get func.
2. Here we are not returning an object instance, but instead a property of an object instance.
"""
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
        
