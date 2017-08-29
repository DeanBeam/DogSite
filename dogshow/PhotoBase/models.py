from django.db import models
from DogBase.models import Dog
from django import template

register = template.Library()

# Create your models here.

class dogImage(models.Model):
	"""docstring for dogImage"""
	imageDog = models.ImageField(upload_to='DogImages')
	imageTag = models.ManyToManyField(Dog)
	imageDate = models.DateField()
	imageForFace = models.BooleanField()

	# @register.tag(name="filterDog")
	# def get_filtered_dogs(parser, token):
	# 	try:
	# 		tag_name, dog = token.split_contents()
	# 	except ValueError:
	# 		raise template.TemplateSyntaxError("%r tag requires a single dog object" % token.contents.split()[0])
	# 	return FilterDogNode(dog)

	# class FilterDogNode(template.Node):

	# 	def __init__(self, imageDog):
	# 		self.imageDog = imageDog

	# 	def render(self, context):
	# 		things = context['images']
	# 		answers = things.objects.filter(imageTag = context)
	# 		return answers

	def __str__(self):
		return str(self.pk)



	# @register.assignment_tag
	# def filterDog(,Dog):
	# 	# dog = context['dog']
	# 	# answers2 = dogImage.objects.filter(imageTag = dog)
	# 	answers = dogImage.objects.filter(imageTag = Dog) 		
	# 	return {"filterDog": answers2}

	# @register.filter
	# def filterDog(thing, Dog):
	# 	return thing.objects.filter(imageTag = Dog) 

		