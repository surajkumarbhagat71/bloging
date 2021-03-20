from django.urls import path
from blog.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',Home.as_view(),name="home"),
    path("blogdetail&&/<int:pk>",BlogDetail.as_view(),name = "blogdetail"),
    path('catblog/<int:pk>',CategoryBlog.as_view(),name = 'catblog'),
    path('signup',Signup.as_view(),name="signup"),
    path('login/',Login.as_view(),name="login"),
    path('logout',Logout.as_view(),name ="logout"),
    path('search',Search.as_view(),name ="serach"),
    path('addblog',AddNewArticle.as_view(),name="addblog"),
    path('allarticle',MyAllArticle.as_view(),name="allarticle"),
    path('deletearticle/<int:pk>',DeleteArticle.as_view(),name="deletearticle"),
    path('adduserdetail',AddUserDetail.as_view(),name = 'adduserdetail'),
    path('profile',Profile.as_view(),name = "profile"),
    path('updateprofile/<int:pk>',ProfileUpdate.as_view(),name="updateprofile"),
    path('blogofprofile/<int:pk>',BlogofProfile.as_view(),name="blogofprofile"),
    path('like/<int:pk>',Likes.as_view(),name="like"),
    path('comments/<int:pk>',Comment.as_view(),name="comments"),
    path('about',About.as_view(),name="about"),



    #----------------------------------- forget passwrod -----------------------#

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
