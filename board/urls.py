from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from board.handlers import BoardHandler, StageHandler, StoryHandler

board_resource = Resource(handler=BoardHandler)
stage_resource = Resource(handler=StageHandler)
story_resource = Resource(handler=StoryHandler)

urlpatterns = patterns('',
    url(r'^$', 'scrumboard.board.views.board', name='board'),
    url(r'^api/stage/$', stage_resource),
    url(r'^api/stage/(?P<id>[^/]+)$', stage_resource),
    url(r'^api/story/$', story_resource,),
    url(r'^api/story/(?P<id>[^/]+)$', story_resource,),
    url(r'^api/board/$', board_resource),
    url(r'^api/board/(?P<id>[^/]+)$', board_resource),
)
