from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('posts/<int:pk>/', views.CommentDetail.as_view())
]