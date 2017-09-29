from django.db import models

# Create your models here.


class News(models.Model):
	title = models.CharField(max_length= 500)
	body = models.TextField()
	timefield = models.DateTimeField()
	image = models.ImageField(upload_to='NewsImages')
	

	def __str__(self):
		return self.title

	def get_year(self):
		return str(self.timefield.year)