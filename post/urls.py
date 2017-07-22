from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.author_list, name='author_list'),
    url(r'^(?P<id>\d+)/$', views.author_detail, name='author_detail'),
    url(r'^update/(?P<id>\d+)/$', views.author_update, name='author_update'),
    url(r'^add/$', views.author_add, name='author_add'),
]