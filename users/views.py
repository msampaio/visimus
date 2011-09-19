import subprocess
import django
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import os
import settings


def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect("/")


@login_required
def dashboard(request):
    args = {}
    
    return render(request, 'dashboard.html', args)


@login_required
def deploy(request):
    if settings.PRODUCTION:
        deployment_dir = "/home/kroger/webapps/visimus/visimus/deployment"
        result = subprocess.call(os.path.join(deployment_dir, "update-server.sh"))
    else:
        result = "deploy new version"

    print result
    # TODO: use ajax to update page
    #return HttpResponse(result)
    return HttpResponseRedirect(reverse(dashboard))
