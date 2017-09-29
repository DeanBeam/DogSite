from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from news.models import News

# Create your views here.


def index(request, **kwargs):
	
	indexNews = News.objects.all()
	ListOfYears = set()
	for novost in indexNews:
		if novost.get_year() not in ListOfYears:
			ListOfYears.add(novost.get_year())
	if kwargs.get('year'):
		indexedNews = []
		for n in indexNews:
			if n.get_year() == kwargs.get('year'): indexedNews.append(n)	
		if not indexedNews:
			return redirect('index')
		indexNews = indexedNews

	paginator = Paginator(indexNews,5)
	page = request.GET.get('page')

	try:
		listNews = paginator.page(page)
	except PageNotAnInteger:
		listNews = paginator.page(1)
	except EmptyPage:
		listNews = paginator.page(paginator.num_pages)

	return render(request, 'news/1index.html',{'news':listNews, 'years':sorted(ListOfYears, reverse=True)})



def contacts(request):
	return render(request, "contacts.html")