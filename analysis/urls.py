from django.urls import path
from . import views

urlpatterns = [
	path("", views.analyze_text, name = "analyze_text"),
	path("signup/", views.signup, name = "signup"),
]