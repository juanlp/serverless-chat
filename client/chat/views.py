from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import render
from uniauth.decorators import login_required
import requests

@receiver(user_logged_in)
def register_session(sender, request, user, **kwargs):
    if request.session.exists:
        data = {
            "secret": "SHARED_SECRET",
            "sessionid": request.session.session_key,
            "username": user.username
        }
        response = requests.post(("https://jy004objlc.execute-api.us-east-1"
                ".amazonaws.com/dev/register_session"), json=data)

@login_required
def index(request):
    return render(request, 'chat/index.html')

