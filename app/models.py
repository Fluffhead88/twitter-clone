from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class File(models.Model):
    file = models.FileField(upload_to='static/uploads',
                            blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=140, default="No tweet body provided")
    created = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/uploads', verbose_name='image')

    def likes(self):
        from app.serializers import LikeSerializer
        serialized_likes = LikeSerializer(self.like_set, many=True)
        return serialized_likes.data


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
