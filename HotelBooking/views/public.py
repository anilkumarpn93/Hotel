from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.views import generic
from HotelBooking.models import login
from HotelBooking.forms import LoginForm,UserForm

# Create your views here.
def home(request):
	return render(request,'public/home.html')

# def login_public(request):
# 	return render(request,'public/login.html',context)


class HomeView(generic.TemplateView):
	template_name = 'public/home.html'


class LoginView(generic.View):
	template_name = 'public/login.html'
	def get(self,request):
		return render(request,self.template_name,{"login_form":LoginForm,'user_form':UserForm})
	def post(self,request):
		loginForm = LoginForm(request.POST)
		userForm = UserForm(request.POST)
		if all([loginForm.is_valid(),userForm.is_valid()]):
			loginForm.save()
			userForm.login = loginForm
			userForm.save()
		else:
			print("Error")
		return render(request,self.template_name,{})


