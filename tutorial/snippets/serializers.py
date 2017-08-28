from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    """
    Creating new serializer class by inheriting ModelSerializer class.
    This will help us avoid replicating all information from Snippet Model.
    (Better than Serializer class)
    *An automatically determined set of fields.
    *Simple default implementations for the create() and update() methods.
    """
    class Meta:
        model = Snippet
        """
        fields= (), tells about what fields are to be sent in response.
        To send all the fields available in Model, use fields '__all__'.
        """
        fields =  ('id','title','code','linenos','language','style')
        #fields = '__all__'
        """
        adding this to reflect association of Snippets & Users.
        """
        owner = serializers.ReadOnlyField(source='owner.username')

        """
        The field we've added is the untyped ReadOnlyField class,
        in contrast to the other typed fields, such as CharField, BooleanField etc...
        The untyped ReadOnlyField is always read-only, and will be used for serialized representations,
        but will not be used for updating model instances when they are deserialized.
        We could have also used CharField(read_only=True) here.
        """
        
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    """
    'snippets' is a reverse relationship on the User model,
    it will not be included by default when using the ModelSerializer class,
    so we needed to add an explicit field for it.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
