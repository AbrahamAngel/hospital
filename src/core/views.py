from django.shortcuts import render

def login_page_view(request):
	return render(request, 'directory/login.html')
