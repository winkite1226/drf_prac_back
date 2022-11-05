from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from articles.serializers import ArticleSerializer, ArticleCreateSerializer
from articles.models import Article

# 게시글 보기/작성하기
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post_author=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 

# 게시글 상세보기/수정하기/삭제하기
class ArticleDetailView(APIView):
    def get(self, request, article_id):
        pass
    def put(self, request, article_id):
        pass
    def delete(self, request, article_id):
    	pass

# 댓글 보기/작성하기
class CommentView(APIView):
    def get(self, request, article_id):
        pass
    def post(self, request, article_id):
    	pass

# 댓글 수정하기/삭제하기
class CommentDetailView(APIView):
    def put(self, request, article_id, comment_id):
        pass
    def delete(self, request, article_id, comment_id):
    	pass

# 게시글 좋아요
class LikeView(APIView):
    def post(self, request, article_id):
        pass