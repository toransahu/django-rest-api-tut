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

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


    ##@detail_route decorator to create a custom action, named highlight.
    ##This decorator can be used to add any custom endpoints
    ##that don't fit into the standard create/update/delete style.
    ##
    ##Custom actions which use the @detail_route decorator will respond to GET requests by default.
    ##We can use the methods argument if we wanted an action that responded to POST requests.
    ##
    ##The URLs for custom actions by default depend on the method name itself.
    ##If you want to change the way url should be constructed,
    ##you can include url_path as a decorator keyword argument.

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
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
