from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics



# Create your views here.

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all snippets, or crete a new snippet.

    The base class provides the core functionality,
    and the mixin classes provide the .list() and .create() actions.
    We're then explicitly binding the get
    and post methods to the appropriate actions.
    """
    
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request, *args, **kwargs)
            

    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs)
    
    
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a snippet instance.

    Adding in mixins to provide the .retrieve(), .update() and .destroy() actions.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
