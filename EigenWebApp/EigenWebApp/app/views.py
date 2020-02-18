"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from app.nlp.InterestingWordManager import InterestingWordManager

def home(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    interesting_words = InterestingWordManager()
    interesting_terms = interesting_words.get_interesting_terms()
    return render(
        request,
        'app/index.html',
        {
            'title':'Interesting Word Extractor',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'interesting_terms':interesting_terms
        }
    )
