""" board views """

from django.shortcuts import render_to_response
from scrumboard.settings.local import STATIC_URL


def app(request):
    """ app request """
    return render_to_response("board/app.html", {"STATIC_URL": STATIC_URL})


def home(request):
    """ home request """
    return render_to_response("index.html", {"STATIC_URL": STATIC_URL})
