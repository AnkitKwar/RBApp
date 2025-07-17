from django.shortcuts import render, HttpResponse

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
