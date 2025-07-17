from django.shortcuts import render, HttpResponse
from django.http import Http404

# Create your views here.

def home(request):
#    return HttpResponse("Hello, World!")
     return render(request, 'home.html')

def regex_topics(request):
    topics = [
        ('Anchors', '/regex/anchors'),
        ('Character Classes', '/regex/charclasses'),
        ('Quantifiers', '/regex/quantifiers'),
        ('Groups', '/regex/groups'),
        ('Lookahead/Lookbehind', '/regex/lookaround'),
        ('Regex Cheatsheet', '/regex/cheatsheet'),
    ]
    return render(request, 'regex_topics.html', {'topics': topics})

def topic_detail(request, topic_name):
    if topic_name not in ['anchors', 'quantifiers']:
        raise Http404("Topic not found")
    return render(request, 'topic_detail.html', {'topic': topic_name})
