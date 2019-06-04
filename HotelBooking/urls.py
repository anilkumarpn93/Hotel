from django.urls import path
from .views.public import ( 
	home,
	LoginView,
	register_user,
	register_hotel
)
app_name = 'booking'
urlpatterns = [
	path('',home,name='home'),
	path('login/',LoginView.as_view(),name='login'),
	path('register_user/',register_user,name='register_user'),
	path('register_hotel/',register_hotel,name='register_hotel')
]


