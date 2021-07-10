from django.urls import path
from home.views import Addpost, Index, ViewPost

urlpatterns = [
    path('', Index.as_view(), name = "home"),
    path('addpost', Addpost.as_view(), name = "addpost"),
    path('viewpost', ViewPost.as_view(), name = "viewpost")
]