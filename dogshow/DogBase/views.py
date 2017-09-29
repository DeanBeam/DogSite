from django.shortcuts import render,render_to_response
from DogBase.models import Dog, TypeDog
from PhotoBase.models import dogImage

# Create your views here.


def labrador_view(request, dogtype):
	labraDogsBoys = Dog.objects.filter(dogType = TypeDog.objects.get(typeSlug=dogtype)).filter(dogSex="M")
	labraDogsGirls = Dog.objects.filter(dogType = TypeDog.objects.get(typeSlug=dogtype)).filter(dogSex="F")
	dogImagesB = dogImage.objects.filter(imageForFace=True).filter(imageTag__in=labraDogsBoys)
	dogImagesG = dogImage.objects.filter(imageForFace=True).filter(imageTag__in=labraDogsGirls)
	return render(request, "DogBase/labradors.html", {'boys':labraDogsBoys, 'girls':labraDogsGirls, 'imagesB':dogImagesB, 'imagesG':dogImagesG})


def detail_view(request, dogtype,dogSlug):
	deatailDog = Dog.objects.get(dogSlug = dogSlug)
	photosOfDog = dogImage.objects.filter(imageTag = deatailDog)
	return render(request, "DogBase/detailDog.html", {"dog":deatailDog, "images": photosOfDog})