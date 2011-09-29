# Create your views here.
 
from django.shortcuts import  render_to_response
 
 
def home(request):
    """ """
    c = {}
    c.update({"user": request.user})
    return render_to_response("home.html", c)
