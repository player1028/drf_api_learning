from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women
from .serializers import WomenSerializer
from rest_framework import generics, viewsets




class WomenViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer




'''class WomenAPIList(generics.ListCreateAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer



class WomenAPIUpdate(generics.UpdateAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer'''



'''class WomenAPIView(APIView):

	def get(self, request):
		w = Women.objects.all()
		w = WomenSerializer(w, many=True)
		return Response({"posts": w.data})


	def post(self, request):
		serializer = WomenSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({"posts": serializer.data})


	def put(self, request, *args, **kwargs):
		pk = kwargs.get("pk", None)
		if not pk:
			return Reponse({"error": "Method PUT not allowed"})
		try:
			instance = Women.objects.get(pk=pk)
		except:
			return Reponse({"error": "Method PUT not allowed"})

		serializer = WomenSerializer(data=request.data, instance=instance)
		serializer.is_valid()
		serializer.save()
		return Response({"posts": serializer.data})


	def delete(self, request, *args, **kwargs):
		pk = kwargs.get("pk", None)
		if not pk:
			return Response({"error": "Method DELETE not allowed"})
		try:
			instance = Women.objects.get(pk=pk)
			instance.delete()
		except:
			return Response({"error": "Method DELETE not allowed"})
		return Response({"posts": "deleted posts " + str(pk)})


'''

#class WomenAPIView(generics.ListAPIView):
#	queryset = Women.objects.all()
#	serializer_class = WomenSerializer