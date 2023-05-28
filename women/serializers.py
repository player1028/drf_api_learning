from rest_framework.serializers import Serializer 
from .models import Women
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers


class WomenModel:
	def __init__(self, title, content):
		self.title = title
		self.content = content




class WomenSerializer(Serializer):
	title = serializers.CharField(max_length=200)
	content = serializers.CharField()




def encode():
	model = WomenModel("Angelina Jolie", "Content: Angelina Jolie")
	model_sr = WomenSerializer(model)
	print(model_sr.data, type(model_sr.data))
	json = JSONRenderer().render(model_sr.data)
	print(json)


def decode():
	stream = io.BytesIO(b"{'title':'Angelina Jolie','content':'Content: Angelina Jolie'}")
	data = JSONParser().parse(stream)
	serializer = WomenSerializer(data=data)
	  