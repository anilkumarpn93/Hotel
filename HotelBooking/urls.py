from django.urls import path
from .views.public import ( 
	HomeView,
	LoginView
)
app_name = 'booking'
urlpatterns = [
	path('',HomeView.as_view(),name='home'),
	path('login/',LoginView.as_view(),name='login'),
	
]


