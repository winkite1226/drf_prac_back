from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    post_author = serializers.SerializerMethodField()

    #반드시 get_위의변수명 이어야 한다.
    def get_post_author(self, obj):
        return obj.post_author.username

    class Meta:
        model = Article
        fields = '__all__'

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("post_title", "post_restaurant", "post_content", "post_image")