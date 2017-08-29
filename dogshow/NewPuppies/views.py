from django.shortcuts import render,render_to_response
from NewPuppies.models import Pair,imagesPair
# Create your views here.


def weSharePuppies_view(request):
	weHavePuppies = Pair.objects.filter(pairWanted=False).filter(pairIsPast=False)
	weWaitPuppies = Pair.objects.filter(pairWanted=True).filter(pairIsPast=False)
	return render_to_response("NewPuppies/listPairs.html", {"havePuppies": weHavePuppies, "waitPuppies": weWaitPuppies})

def weHadGrowth_view(request):
	weHadGrowth = Pair.objects.filter(pairIsPast=True)
	return render_to_response("NewPuppies/growthPuppies.html", {"havePuppies": weHadGrowth})


def photoPuppies_detailview(request, pairLiter):
	lookedPair = Pair.objects.get(pairLiter=pairLiter)
	images = imagesPair.objects.filter(imagePairTag = lookedPair)
	return render_to_response("NewPuppies/photoLib.html", {"images":images, "pair":lookedPair})
