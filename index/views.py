from django.shortcuts import render

def index(request):
	return render(request, 'index/index.html')


def shop(request):
	return render(request, 'index/shop.html')