from django.shortcuts import render

#HOME PAGE ###########################################################################
def home(request):
	return render(request, "home.html");
