from django.db import models
from users.models import User

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = 'article'

    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    post_restaurant = models.CharField(max_length=30)
    post_content = models.TextField()
    post_image = models.ImageField(blank=True, upload_to="$Y/%m")
    post_like = models.ManyToManyField(User, related_name="like_articles")
    post_created = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post_title)


class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_postid = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment_set")
    comment_content = models.TextField()
    comment_created = models.DateTimeField(auto_now_add=True)
    comment_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment_content)
