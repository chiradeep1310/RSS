from django.shortcuts import render
from django.http import HttpResponse
import feedparser

def index(request):
    url = "http://rss.cnn.com/rss/edition.rs"
    feed = feedparser.parse(url)
    print(feed.feed.links)
    return render(request,'blog/about.html',{"feed": feed })
