from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r"womenlist", views.WomenViewSet)


urlpatterns = [
	path('v1/', include(router.urls)),
	#path('v1/womenlist/', views.WomenViewSet.as_view({'get': 'list'})),
	#path('v1/womenlist/<int:pk>/', views.WomenViewSet.as_view({'put': 'update'})),
	#path('v1/womendetail/<int:pk>/', views.WomenViewSet.as_view({'delete': 'delete'})),
#	path('v1.0.0/womenlist/', views.WomenAPIView.as_view()),
#	path('v1.0.0/womenlist/<int:pk>/', views.WomenAPIView.as_view()),
]