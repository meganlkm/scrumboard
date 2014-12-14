""" board admin """

from django.contrib import admin
from scrumboard.board.models import Board, Stage, Story


class StageInline(admin.TabularInline):

    """ stage in line """

    model = Stage


class BoardAdmin(admin.ModelAdmin):

    """ board admin """

    inlines = [StageInline, ]


class StoryInline(admin.TabularInline):

    """ story in line """

    model = Story


class StageAdmin(admin.ModelAdmin):

    """ stage admin """

    inlines = [StoryInline, ]

admin.site.register(Stage, StageAdmin)
admin.site.register(Board, BoardAdmin)
