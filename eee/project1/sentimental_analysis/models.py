from django.db import models

class AnalyzedSentence(models.Model):
    sentence = models.TextField()
    emotion = models.CharField(max_length=50)
    sentiment = models.CharField(max_length=20)
    emoji = models.CharField(max_length=10)
