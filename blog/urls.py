from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #name kann nachher über templatetag % post_list % aufgerufen werden
    #views.post_list greift auf def(post_list(reuqest) in views.py zu)
        path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
