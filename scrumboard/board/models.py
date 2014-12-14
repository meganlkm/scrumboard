""" board models """

from django.conf import settings
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.encoding import smart_text


class Board(models.Model):

    """ board model """

    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        """ unicode """
        return smart_text(self.title)

    def save(self, *args, **kwargs):
        """ save the board """
        return super(Board, self).save(*args, **kwargs)


class Stage(models.Model):

    """ stage model """

    board = models.ForeignKey(Board)
    order = models.IntegerField()
    title = models.CharField(max_length=30, choices=settings.STAGE_CHOICES)

    class Meta:
        ordering = ["order", ]

    def __unicode__(self):
        """ unicode """
        return smart_text(self.title)


class Story(models.Model):

    """ story model """

    stage = models.ForeignKey(Stage)
    description = models.TextField()
    color = models.CharField(max_length=30, choices=settings.COLOR_CHOICES)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ["order", ]

    def save(self, **kwargs):
        """ save """
        if self.pk and not self.order:
            # self.order = (
            #     self.stage.story_set.aggregate(
            #         Max("order")).get("order__max") or 0)  + 1
            # TODO: use aggregate for performance !
            from operator import attrgetter
            try:
                total = max(
                    self.stage.story_set.all(),
                    key=attrgetter("order")) + 1
            except ValueError:
                total = 1
            self.order = total
            self.save()
        super(Story, self).save(**kwargs)

    def __unicode__(self):
        """ unicode """
        return smart_text(self.description)


def create_stages(sender, **kwargs):
    """ create stages """
    if kwargs.get("created"):
        instance = kwargs["instance"]
        for order, stage in enumerate(settings.STAGE_CHOICES):
            key, label = stage
            instance.stage_set.get_or_create(order=order, title=key)


post_save.connect(create_stages, sender=Board)
