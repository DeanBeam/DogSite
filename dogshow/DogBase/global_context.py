from DogBase.models import TypeDog

def base_context(request):
	typeDog = TypeDog.objects.all()
	return {'dogType': typeDog}