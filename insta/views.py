from urllib import request
from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Comments, Images, Profile, CustomUser, Like
from .forms import UpdateProfileForm, ImagesForm, CommentsForm
from django.contrib.auth.models import User


# Create your views here.
"""
View for home page. It requires one to be logged in inorder to access
"""
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    images = Images.objects.all().order_by("date_posted").reverse()
    liked_images = [i for i in Images.objects.all() if Like.objects.filter(user = request.user, image=i)]


    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.profile = Profile.objects.get(user_id = current_user.id)
            image.save()

        return redirect("home") 

    else:
        form = ImagesForm()    

    return render(request, 'home.html', {"current_user":current_user, "images": images, "form":form, "liked_images":liked_images})
"""
View for creating profile page if you are a new user
"""

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user

    try:
        Profile.objects.get(user_id = current_user.id)
        return redirect("home")

    except:

        if request.method == 'POST':
            form = UpdateProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit = False)
                profile.user = current_user
                profile.save()

            return redirect("home")   

        else:
            form = UpdateProfileForm()

    return render(request, 'create_profile.html', {"form": form, "current_user":current_user})    
"""
View for profile page of the current user
"""
@login_required(login_url='/accounts/login/')
def profile(request, username):
    current_user = request.user
    profile =  Profile.objects.filter(user = CustomUser(id = current_user.id)).first()
    images = Images.objects.filter(profile = profile.pk ).all() 
        
    return render(request, 'profile.html', {"profile": profile, "images": images, "current_user": current_user})   

"""
View for uploading images
"""

@login_required(login_url='/accounts/login/')
def upload_images(request):
    current_user = request.user

    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.profile = Profile.objects.get(user_id = current_user.id)
            image.save()

        return redirect("home")   

    else:
        form = ImagesForm()

    return render(request, 'images.html', {"form": form, "current_user":current_user})    
"""
View for following and unfollowing
"""
@login_required(login_url='/accounts/login/')
def followToggle(request, user):

    userObj = CustomUser.objects.filter(username = user).first()
    current_user = request.user
    current_user.follow_user(userObj)

    return redirect('viewProfile', username = userObj.username )        

"""
View for searching for users by their username"
"""
@login_required(login_url='/accounts/login/')
def search_profile(request):
      current_user = request.user
      if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_profile": searched_profile, "current_user":current_user})

      else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message, "current_user":current_user})

"""
View for adding a comment it takes in the argument of image id
"""
@login_required(login_url='/accounts/login/')
def comment(request, id):
     image = Images.objects.get(id = id)
     current_user = request.user

     if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.commentor = current_user
            comment.image = image
            comment.save()

        return redirect("home")   

"""
View for viewing someone's profile from homepage
"""
@login_required(login_url='/accounts/login/')
def view_profile(request, username):
    current_user = request.user
    user = CustomUser.objects.get(username = username)
    profile =  Profile.objects.filter(user = CustomUser(id = user.id)).first()
    images = Images.objects.filter(profile = profile.pk ).all() 


    return render(request, 'users_profile.html', {"profile": profile, "images":images, "current_user":current_user, "user":user})

"""
View for liking images
"""
@login_required(login_url='/accounts/login/')
def like(request, id):
    current_user = request.user
    image = Images.objects.get(pk=id)
    like = Like.objects.filter(user=current_user, image = image).first()
    if like:
        like.delete()
    else:
        print(current_user, image)
        new_like = Like(user=current_user, image=image)
        new_like.save()

    return redirect('home')


