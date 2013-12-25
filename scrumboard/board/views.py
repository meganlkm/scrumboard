from django.shortcuts import render_to_response
#from django.template.context import RequestContext
#from scrumboard.core.decorators import render_template
from scrumboard.settings import STATIC_URL

def app(request):
    return render_to_response("board/app.html",{"STATIC_URL":STATIC_URL})

def home(request):
    return render_to_response("index.html",{"STATIC_URL":STATIC_URL})