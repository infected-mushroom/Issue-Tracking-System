from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
      # ex: /boards/5/lists
    url(r'^(?P<board_id>[0-9]+)/lists/$', views.board_content, name='board_content'),
    # ex: /boards/5/lists/1
    url(r'^(?P<board_id>[0-9]+)/lists/(?P<list_id>[0-9]+)/$', views.list_content, name='list_content'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
