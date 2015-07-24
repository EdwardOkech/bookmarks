from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

def main_page(request):
    template = get_template('main_page.html')
    var = Context({'head_title': 'Django bookmarks'})
    output = template.render(var)
    return HttpResponse(output)

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('User not found')
    bookmarks = user.bookmark_set.all()
    template = get_template('user_page.html')
    var = Context({'username':username, 'bookmarks':bookmarks})
    output=template.render(var)
    return HttpResponse(output)

# Create your views here.
