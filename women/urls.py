from django.urls import path
from . import views



urlpatterns = [
	path('v1.0.0/womenlist/', views.WomenAPIView.as_view()),
]