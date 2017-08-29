from django.shortcuts import render,render_to_response
from news.models import News

# Create your views here.


def index(request):
	indexNews = News.objects.all()
	return render(request, 'news/index.html',{'news':indexNews})

def contacts(request):
	return render_to_response("contacts.html")