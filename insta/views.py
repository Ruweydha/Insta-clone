from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    return render(request, 'home.html', {"current_user": current_user})
