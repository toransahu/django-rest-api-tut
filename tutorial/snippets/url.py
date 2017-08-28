from django.conf.urls import url
from snippets import views
"""
to append a set of format_suffix_patterns in addition to the existing URLs.
"""
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$',views.snippet_list),
    url(r'^(?P<pk>[0-9]+)/$',views.snippet_detail),
]

"""
to append a set of format_suffix_patterns in addition to the existing URLs.
"""
urlpatterns = format_suffix_patterns(urlpatterns)
