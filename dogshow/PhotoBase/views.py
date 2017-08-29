from django.shortcuts import render, render_to_response
from PhotoBase.models import dogImage
# Create your views here.


def allPhotos_view(request):
	allPhotosObjects = dogImage.objects.all()
	context = base_context(request)
	return render_to_response("photoBase/allPhotos.html", {"images":allPhotosObjects})