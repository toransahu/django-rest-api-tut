from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views


"""
Routers is simple tool to speed-up implementing of API.
Using Router will connect your ViewSet into "standarized"
(it's not standard in any global way,
just some structure that was implemented
by creators of Django REST framework)
structure of URLs.
That way you don't have to create your urlpatterns by hand and
you're guaranteed that all of your urls are consistent.
"""

"""
There are two mandatory arguments to the register() method:

prefix - The URL prefix to use for this set of routes.
viewset - The viewset class.
Optionally, you may also specify an additional argument:

base_name - The base to use for the URL names that are created.

URL pattern: ^users/$ Name: 'user-list'
URL pattern: ^users/{pk}/$ Name: 'user-detail'
URL pattern: ^accounts/$ Name: 'account-list'
URL pattern: ^accounts/{pk}/$ Name: 'account-detail'
"""


"""
Because we're using viewsets instead of views, we can automatically generate the URL conf for our API, by simply registering the viewsets with a router class.

Again, if we need more control over the API URLs we can simply drop down to using regular class-based views, and writing the URL conf explicitly.

Finally, we're including default login and logout views for use with the browsable API. That's optional, but useful if your API requires authentication and you want to use the browsable API.
"""

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^',include(router.urls)),
]
