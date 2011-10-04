# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from chenkmail.apps.namelist.models import Professor

@login_required(login_url='/mail/login')
def index(request):

    data_table = {}
    data_table['professors'] = Professor.objects.all()
    data_to_render = RequestContext(request, data_table)
    return render_to_response('base.html', data_to_render)
