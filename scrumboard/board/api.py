""" board api """

from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields
from scrumboard.board.models import Story, Board, Stage


class BoardResource(ModelResource):

    """ board resource """

    def obj_create(self, bundle, request=None, **kwargs):
        """ create object """
        # TODO: Authentication
        kwargs["user_id"] = 1
        return super(BoardResource, self).obj_create(bundle, **kwargs)

    class Meta:
        queryset = Board.objects.all()
        resource_name = 'board'
        #include_resource_uri = False
        authorization = Authorization()


class StageResource(ModelResource):

    """ stage resource """

    board = fields.ForeignKey(BoardResource, 'board', full=True)

    class Meta:
        queryset = Stage.objects.all()
        #include_resource_uri = False
        authorization = Authorization()
        filtering = {
            "board": ('exact',)
        }


class StoryResource(ModelResource):

    """ story resource """

    stage = fields.ForeignKey(BoardResource, 'stage', full=True)

    def obj_create(self, bundle, request=None, **kwargs):
        """ create object """
        stage = Stage.objects.get(id=bundle.data.pop("stage")["id"])
        return super(StoryResource, self).obj_create(bundle, stage=stage)

    def obj_update(self, bundle, request=None, **kwargs):
        """ update object """
        story = Story.objects.get(id=kwargs.get("pk"))
        story.description = bundle.data.get("description")
        story.color = bundle.data.get("color")
        story.stage_id = bundle.data.get("stage").get("id")
        story.order = bundle.data.get("order")
        story.save()
        #stage = Stage.objects.get(id=bundle.data.pop("stage")["id"])#
        #return super(StoryResource, self).obj_update(bundle, request)

    class Meta:
        queryset = Story.objects.all()
        #include_resource_uri = False
        authorization = Authorization()
        filtering = {
            "stage": ('exact',)
        }
