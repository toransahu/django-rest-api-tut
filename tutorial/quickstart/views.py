from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets.
    We can easily break these down into individual views if we need to,
    but using viewsets keeps the view logic nicely organized as well as being very concise.

    API endpoint (URL) that allows USERs to be viewed or edited.
    """

    queryset  = User.objects.all().order_by(''-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    Here we have used rest_framework.viewsets instead of django.view.
    This speedups development of API and keep standard behavour.

    Using ViewSet you don't have to create separate views for getting list of objects and detail of one object.
    ViewSet will handle for you in consistent way both list and detail.

    API endpoint (URL) that allows GROUPs to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
