from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women



class WomenAPIView(APIView):

	def get(self, request):
		lst = Women.objects.all().values()
		return Response({'posts': list(lst)})


	def post(self, request):
		new_post = Women.objects.create(title=request.data["title"],
										content=request.data["content"],
										cat_id=request.data["cat_id"])
		return Response({'title': 'H'})





#class WomenAPIView(generics.ListAPIView):
#	queryset = Women.objects.all()
#	serializer_class = WomenSerializer