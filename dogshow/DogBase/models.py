from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class TypeDog(models.Model):
	"""docstring for TypeDog"""
	typeName = models.CharField(max_length=200)
	typeSlug = models.CharField(max_length=100)


	def __str__(self):
		return self.typeName
		


class Dog(models.Model):
	"""This class shows the dogs"""
	dogName = models.CharField(max_length = 400)
	dogShortName = models.CharField(max_length = 200)
	dogSlug = models.SlugField()
	dogBday = models.DateField()
	dogDef = models.TextField()
	dogType = models.ForeignKey(TypeDog)
	dogPath = models.CharField(max_length=200)
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
		)
	dogSex = models.CharField(max_length=1, choices=GENDER_CHOICES)
	dogIsPuppy = models.BooleanField()
	dogIsOurs = models.BooleanField()
		
	def __str__(self):
		return self.dogName

	def save(self, *args, **kwargs):
		self.dogSlug = slugify(self.dogShortName)
		super(Dog, self).save(*args, **kwargs)
