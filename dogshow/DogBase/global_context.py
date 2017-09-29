from DogBase.models import TypeDog
from news.models import News

def base_context(request):
	typeDog = TypeDog.objects.all()
	return {'dogType': typeDog}