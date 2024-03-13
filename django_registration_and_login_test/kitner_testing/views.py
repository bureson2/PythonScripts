from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
from django.http import HttpResponse
from django.contrib.auth.models import User

@csrf_exempt
def register(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        if request_body['password'] == request_body['passwordAgain']:
            new_user = User.objects.create_user(username=request_body['username'],
                                            email=request_body['email'],
                                            password=request_body['password'])
            new_user.save()
            return HttpResponse(status=200)
    return HttpResponse(status=400)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        username = request_body['username']
        password = request_body['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
    return HttpResponse(status=400)

def csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrf_token': token})

@login_required
def home(request):
    return render(request, 'home.html')
