from django.urls import path
from comments_likes import views


urlpatterns = [
    path('comments_likes/', views.ListCommentLikes.as_view()),
    path('comments_likes/<int:pk>', views.DetailCommentLikes.as_view())
]
