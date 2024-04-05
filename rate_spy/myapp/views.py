from django.shortcuts import render

# Create your views here.
def index_view(request):
		# Add your view logic here
		context = {
			'message': 'Hello, world!'
		}
		return render(request, 'index.html', context)