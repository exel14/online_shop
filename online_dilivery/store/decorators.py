from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group

def unauth_user(view_func):
    def wrapped(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapped

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapped(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('You have no permission!')
        return wrapped
    return decorator

def admin_only(view_func):
    def wrapped(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('user')
        if group == 'manager':
            return view_func(request,*args,**kwargs)
    return wrapped