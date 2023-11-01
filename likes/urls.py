from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('posts/<int:pk>/', views.CommentDetail.as_view())
]