from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.views import View,generic
from HotelBooking.models import login
# Create your views here.
def home(request):
	return render(request,'public/home.html')

# def login_public(request):
# 	return render(request,'public/login.html',context)


class LoginView(generic.ListView):

	context_object_name = 'login'
	def get_queryset(self):
		return login.objects.all()



def register_user(request):
	return render(request,'public/login.html')

def register_hotel(request):
	return render(request,'public/login.html')


