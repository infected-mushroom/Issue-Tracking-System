from django.conf.urls import url

from . import views

app_name = 'boards'
urlpatterns = [
    url(r'^$', views.index, name='index'),
      # ex: /boards/5/lists
    url(r'^(?P<board_id>[0-9]+)/lists/$', views.board_content, name='board_content'),
    # ex: /boards/5/lists/1
    url(r'^(?P<board_id>[0-9]+)/lists/(?P<list_id>[0-9]+)/$', views.list_content, name='list_content'),
    url(r'^new/$', views.board_new, name='board_new'),
    url(r'^(?P<board_id>[0-9]+)/lists/new/$', views.list_new, name='list_new'),
    url(r'^(?P<board_id>[0-9]+)/lists/(?P<list_id>[0-9]+)/task_new/$', views.task_new, name='task_new'),
    url(r'^(?P<board_id>[0-9]+)/lists/edit/$', views.board_edit, name='board_edit'),
    url(r'^(?P<board_id>[0-9]+)/lists/(?P<list_id>[0-9]+)/edit/$', views.list_edit, name='list_edit'),
    url(r'^(?P<board_id>[0-9]+)/lists/remove/$', views.board_remove, name='board_remove'),
    url(r'^(?P<board_id>[0-9]+)/lists/(?P<list_id>[0-9]+)/remove/$', views.list_remove, name='list_remove'),
#    url(r'^(?P<board_id>[0-9]+)/lists/(?P<list_id>[0-9]+)/comment/$', views.add_comment_to_task, name='add_comment_to_task'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
