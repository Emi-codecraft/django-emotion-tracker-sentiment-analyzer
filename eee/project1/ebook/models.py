# in models.py within your app
from django.db import models

class Emotion(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=20)
    sentiment_score = models.FloatField()
