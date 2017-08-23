from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


'''"""
Commenting out this because:
Our SnippetSerializer class is replicating a lot of information that's also contained in the Snippet model. It would be nice if we could keep our code a bit more concise.

In the same way that Django provides both Form classes and ModelForm classes, REST framework includes both Serializer classes, and ModelSerializer classes.

class SnippetSerializer(serializers.Serializer):
    """
    The first part of the serializer class defines the fields that get serialized/deserialized. The create() and update() methods define how fully fledged instances are created or modified when calling serializer.save()
    A serializer class is very similar to a Django Form class, and includes similar validation flags on the various fields, such as required, max_length and default.
    The field flags can also control how the serializer should be displayed in certain circumstances, such as when rendering to HTML. The {'base_template': 'textarea.html'} flag above is equivalent to using widget=widgets.Textarea on a Django Form class. This is particularly useful for controlling how the browsable API should be displayed, as we'll see later in the tutorial.
    We can actually also save ourselves some time by using the ModelSerializer class, as we'll see later, but for now we'll keep our serializer definition explicit.
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    """
    validated_data is pre-defined variable, gets initialized when serializer.is_valid() is called.
    """

    def create(self, validated_data):
        """
        Create and return a new 'Snippet' instance, given the validated data.
        """
        # **keyaurgs to a func in python means passing variable number of aurguments to a method with variable name/keywords
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Snippet' instance, given the validated data.

        Here validated_data is an OrderedDict, and OrderedDict.get(key,default) fetches the value
        for given key, returning the default if the key is missing from the dict.
        """
        instance.title = validated_data.get('title',instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
"""
"""'''

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
