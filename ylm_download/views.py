# Create your views here.
 
from django.shortcuts import  render_to_response
from django.core.context_processors import csrf

 
def login(request):
    """ """
    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "login"})
    return render_to_response("test.html", ctx)


def logout(request):
    """
        logout est la views qui permet de se deconnecter
    """

    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "logout"})
    return render_to_response("test.html", ctx)


def owner(request):
    """ """
    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "owner"})
    return render_to_response("test.html", ctx)


def add_owner(request):
    """ """
    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "add_owner"})
    return render_to_response("test.html", ctx)


def edit_owner(request):
    """ """
    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "edit_owner"})
    return render_to_response("test.html", ctx)


def dashboard(request):
    """ """
    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "dashboard"})
    return render_to_response("test.html", ctx)


def gestion_dl(request):
    """ """
    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "gestion_dl"})
    return render_to_response("test.html", ctx)


def add_dl(request):
    """ """
    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "add_dl"})
    return render_to_response("test.html", ctx)


def info_dl(request):
    """ """
    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "info_dl"})
    return render_to_response("test.html", ctx)


def dellete_dl(request):
    """ """
    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "dellete_dl"})
    return render_to_response("test.html", ctx)


def edit_dl(request):
    """ """
    ctx = {}
    ctx.update(csrf(request))
    ctx.update({"page": "edit_dl"})
    return render_to_response("test.html", ctx)

