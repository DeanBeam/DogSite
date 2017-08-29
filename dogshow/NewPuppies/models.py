from django.db import models
from DogBase.models import Dog

# Create your models here.



class Pair(models.Model):
	"""docstring for Pair"""
	pairDate = models.DateField()
	pairLiter = models.CharField(max_length=50)
	pairImage = models.ImageField(upload_to='DogPairImages')
	pairF = models.ForeignKey(Dog, related_name="father")
	pairM = models.ForeignKey(Dog, related_name="mother")
	pairWanted = models.BooleanField()
	pairIsPast = models.BooleanField()
	pairRes = models.TextField()

	def __str__(self):
		return self.pairLiter


class imagesPair(models.Model):
	imagePairName = models.CharField(max_length=200)
	imagePair= models.ImageField(upload_to='DogImages')
	imagePairTag = models.ForeignKey(Pair, on_delete=models.CASCADE)

	def __str__(self):
		return self.imagePairName		