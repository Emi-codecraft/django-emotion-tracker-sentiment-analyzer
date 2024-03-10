from django.shortcuts import render
from textblob import TextBlob

def get_sentiment_score(sentence):
    blob = TextBlob(sentence)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score

def ebook_home(request):
    sentiment_score = None

    if request.method == 'POST':
        sentence = request.POST.get('sentence', '')
        print("Received sentence:", sentence)

        sentiment_score = get_sentiment_score(sentence)
        print("Calculated sentiment score:", sentiment_score)

    return render(request, 'ebook/ebook.html', {'sentiment_score': sentiment_score})
