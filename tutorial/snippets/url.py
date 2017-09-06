from django.conf.urls import url, include
#from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
import snippets
from rest_framework import routers


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
#router = routers.SimpleRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', snippets.views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^',include(router.urls)),
]

"""
to append a set of format_suffix_patterns in addition to the existing URLs.
"""
#urlpatterns = format_suffix_patterns(urlpatterns)
