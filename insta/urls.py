from unicodedata import name
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.home, name = 'home'),
    path('create/profile/', views.create_profile, name = 'create_profile'),
    path('profile/<str:username>/', views.profile, name = 'profile'),
    path('search/username/', views.search_profile, name= 'search_profile'),
    path('comments/image/<int:id>/', views.comment, name= 'comment'),
    path('view/profile/<str:username>', views.view_profile, name = 'viewProfile'),
    path('followToggle/<str:user>', views.followToggle, name = 'followToggle'),
    path('like/<int:id>', views.like, name='like'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)