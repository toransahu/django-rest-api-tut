from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Here we have not used serializer.ModelSerializer.
    But we wanted to implement relationships.
    For relationships we could also use primary key, But
    hyperlinking is good RESTful design.
    """
    class Meta:
        """
        This inner class Meta is an optional.
        Used to add some model metadata to Model class.
        Model metadata is "anything that is not a field"
        ref: https://docs.djangoproject.com/en/dev/topics/db/models/#meta-options
        """
        model = Group
        fields = ('url', 'name')
