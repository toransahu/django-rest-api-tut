from django.conf.urls import url
from snippets import views
"""
to append a set of format_suffix_patterns in addition to the existing URLs.
"""
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$',views.SnippetList.as_view(), name='snippet-list'),
    url(r'^api/$', views.api_root),
    url(r'^(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

]

"""
to append a set of format_suffix_patterns in addition to the existing URLs.
"""
urlpatterns = format_suffix_patterns(urlpatterns)



