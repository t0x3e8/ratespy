from django.shortcuts import render
from .forms import RatingForm

# Create your views here.
def index_view(request):
		# Add your view logic here
		context = {
			'message': 'Hello, world!'
		}
		return render(request, 'index.html', context)

def rating_view(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            # For example, save it to the database
            # You can access form.cleaned_data['link_to_rating_app'] and form.cleaned_data['frequency_of_spy']
            pass
    else:
        form = RatingForm()
    return render(request, 'rating.html', {'form': form})