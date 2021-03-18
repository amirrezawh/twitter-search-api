from django.db import models


class TweetModel(models.Model):
    SearchKeys = models.TextField()
    TweetNumber = models.IntegerField()
    Chart = models.ImageField(upload_to="Pictures")