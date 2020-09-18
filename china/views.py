from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
	return render(request,'index.html',{})

def contact(request):
	if request.method == "POST":
		name =request.POST['name']
		email =request.POST['email']
		subject =request.POST['subject']
		message = request.POST['message']

		#send email
		send_mail(
			name,#subject
			message,#message
			email,#from email
			['samuelfifitini0@gmail.com'],#to email
				 )
		return render(request,'contact.html',{})	
	else:
		return render(request,'contact.html',{})

def blog(request):
	return render(request,'blog.html',{})	


def single_blog(request):
	return render(request,'single_blog.html',{})

def login(request):
	return render(request,'login.html',{})
def tracking(request):
	return render(request,'tracking.html',{})

def elements(request):
	return render(request,'elements.html',{})


def confirmation(request):
	return render(request,'confirmation.html',{})

def registration(request):
	return render(request,'registration.html',{})

def category(request):
	return render(request,'category.html',{})

def cart(request):
	return render(request,'cart.html',{})

def single_product(request):
	return render(request,'single_product.html',{})

def checkout(request):
	return render(request,'checkout.html',{})



