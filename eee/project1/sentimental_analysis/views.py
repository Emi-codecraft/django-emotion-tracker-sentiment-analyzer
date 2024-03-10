from django.shortcuts import render
from django.http import HttpResponse
from textblob import TextBlob
import random

def sentimental_home(request):
    return render(request, 'sentimental_analysis/upload.html', {'emotion': None, 'file_type_error': None})

def analyze_sentiment(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file_content = request.FILES['file'].read().decode('utf-8')
        file_type = determine_file_type(file_content)

        if file_type == 'Text':
            sentences = get_sentences(file_content)
            results = analyze_sentences(sentences)

            return render(request, 'sentimental_analysis/result.html', {'results': results, 'file_type_error': None})
        else:
            return render(request, 'sentimental_analysis/upload.html', {'file_type_error': 'Please select a text file'})
    else:
        return HttpResponse('Invalid request method')

def determine_file_type(content):
    try:
        # Attempt to encode the content to check if it's a text file
        content.encode('utf-8')
        return 'Text'
    except UnicodeEncodeError:
        return 'NotText'

def get_sentences(content):
    blob = TextBlob(content)
    return blob.sentences

def analyze_sentences(sentences):
    results = []

    for sentence in sentences:
        main_concept = get_main_concept(sentence)
        emotion = get_sentiment(main_concept)
        sentiment = 'Positive' if emotion in ['joy', 'happy', 'excited', 'love', 'optimistic'] else 'Not Positive'
        emoji = get_emoji(emotion)

        result = {
            'sentence': str(sentence),
            'emotion': emotion,
            'sentiment': sentiment,
            'emoji': emoji,
        }
        results.append(result)

    return results

def get_main_concept(sentence):
    return ' '.join(str(word) for word in sentence.words)

def get_sentiment(content):
    blob = TextBlob(content)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0.3:
        return 'joy'
    elif sentiment_score < -0.3:
        return 'sadness'
    elif sentiment_score > 0.2:
        return 'happy'
    elif sentiment_score < -0.2:
        return 'angry'
    elif sentiment_score > 0.1:
        return 'excited'
    elif sentiment_score < -0.1:
        return 'disgust'
    elif sentiment_score > 0.05:
        return 'love'
    elif sentiment_score < -0.05:
        return 'fear'
    elif sentiment_score > 0:
        return 'optimistic'
    elif sentiment_score < 0:
        return 'pessimistic'
    elif sentiment_score == 0:
        return 'neutral'
    else:
        return 'unknown'

def get_emoji(emotion):
    emoji_mapping = {
        'joy': '😊',
        'sadness': '😢',
        'happy': '😄',
        'angry': '😠',
        'excited': '😍',
        'disgust': '😷',
        'love': '❤️',
        'fear': '😱',
        'optimistic': '😁',
        'pessimistic': '😎',
        'neutral': '😐',
        'unknown': '❓',
    }

    return emoji_mapping.get(emotion, '❓')
