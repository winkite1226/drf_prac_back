from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticleView.as_view(), name='article_view'),
    path('<int:article_id>/', views.ArticleDetailView.as_view(), name='article_detail_view'),
    path('<int:article_id>/comments/', views.CommentView.as_view(), name='comment_view'),
    path('<int:article_id>/comments/<int:comment_id>/', views.CommentDetailView.as_view(), name='comment_detail_view'),
    path('<int:article_id>/likes/', views.LikeView.as_view(), name='like_view'),
]