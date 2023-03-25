from django.urls import path
from . import views
from .post_view import post_page, index_post
# from .post_view import post_page, index_post, MyTemplateView

urlpatterns = [
    path('root/', views.root),
    path('root/text/', views.text, name="text"),
    path('root/file/', views.file, name="file"),
    path('root/redirect/', views.redirect, name="redirect"),
    path('root/not-allowed/', views.not_allowed, name="not_allowed"),
    path('root/json/', views.json, name="json"),

    path('class-view/', views.MyView.as_view(), name="class_view"),

    # MyTemplateView.as_view()
    path('post/', index_post, name="post"),
    path('post/<int:number>/', post_page, name="posts_list")
]

