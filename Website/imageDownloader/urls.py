from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.homePage, name="homePage"),
]
# media/img3.jpg