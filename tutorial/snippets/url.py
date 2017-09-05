from django.conf.urls import url, include
#from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views 
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^',include(router.urls)),
]

"""
to append a set of format_suffix_patterns in addition to the existing URLs.
"""
#urlpatterns = format_suffix_patterns(urlpatterns)



