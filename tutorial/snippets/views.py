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

from rest_framework import viewsets
from rest_framework.decorators import detail_route

# Create your views here.

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @detail_route(render_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

 
class UserViewSet(viewsets.ReadonlyModelViewSet):
    """
    1. This viewset automatically provides `list` and `detail` actions.

    2. We've used the ReadOnlyModelViewSet class to automatically provide the default 'read-only' operations.
    
    3. REST framework includes an abstraction for dealing with ViewSets,
    that allows the developer to concentrate on modeling the state and interactions of the API,
    and leave the URL construction to be handled automatically, based on common conventions.
    ViewSet classes are almost the same thing as View classes,
    except that they provide operations such as read, or update,
    and not method handlers such as get or put.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    

@api_view(['GET'])
def api_root(request, format=None):
    """
    1. Fucntion-based view for API root URL, using @api_view.
    2. Using 'reverse' to return fully-qualified URLs.
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
  
