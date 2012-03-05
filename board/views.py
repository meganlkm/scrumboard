from django.shortcuts import render_to_response
from django.template.context import RequestContext

def board(request):
    return render_to_response("board/board.html", context_instance=RequestContext(request, {

    }))