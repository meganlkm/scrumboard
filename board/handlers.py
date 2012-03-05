from piston.handler import BaseHandler
from board.models import Board, Stage, Story

class StoryHandler(BaseHandler):
    model = Story
    fields = ('id', 'description', 'color', 'order', 'stage_id')

    def read(self, request, *args, **kwargs):
        _read = super(StoryHandler, self).read(request, *args, **kwargs)
        if 'stage_id' in request.GET:
            return _read.filter(stage__id=request.GET["stage_id"])
        return _read

    def create(self, request, *args, **kwargs):
        attrs = self.flatten_dict(request.data)
        story = Story()
        story.description = attrs["description"]
        story.color = attrs["color"]
        story.stage_id = attrs["stage_id"]
        story.save()
        return story

class StageHandler(BaseHandler):
    model = Stage
    fields = ('id', 'title', 'get_title_display')

    def read(self, request, *args, **kwargs):
        _read = super(StageHandler, self).read(request, *args, **kwargs)
        if 'board_id' in request.GET:
            return _read.filter(board__id=request.GET["board_id"])
        if 'stories' in kwargs:
            return _read.story_set.all()
        return _read


class BoardHandler(BaseHandler):
    model = Board
    fields = ('id', 'title')

    def create(self, request, *args, **kwargs):
        attrs = self.flatten_dict(request.data)
        board = Board()
        board.title= attrs["title"]
        board.user = request.user
        board.save()
        return board