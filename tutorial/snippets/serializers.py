from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    1. Creating new serializer class by inheriting HyperlinkedModelSerializer class.
    2. To use a hyperlinked style between entities.
    (Better than ModelSerializer class)
    3. The HyperlinkedModelSerializer has the following differences from ModelSerializer:
        It does not include the id field by default.
        It includes a url field, using HyperlinkedIdentityField.
        Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    ##  This field is of the same type as the url field,
    ##  except that it points to the 'snippet-highlight' url pattern,
    ##  instead of the 'snippet-detail' url pattern.
    ##  go to url.py and add name='snippet-highlight'
    class Meta:
        model = Snippet
        fields =  ('url', 'id', 'highlight', 'owner',
                   'title','code','linenos','language','style')
        ##  fields= (), tells about what fields are to be sent in response.
        ##  To send all the fields available in Model, use fields = '__all__'.
       
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    
    ##  'snippets' is a reverse relationship on the User model,
    ##  it will not be included by default when using the ModelSerializer or HyperlinkedModelSerializer class,
    ##  so we needed to add an explicit field for it.
    ##  Go to url.py and add name='snippet-detail'
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
