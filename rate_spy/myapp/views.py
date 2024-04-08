from django.shortcuts import render
from django.contrib import messages
from .forms import RatingForm
from .utils import save_to_database, process_form_data


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
            save_to_database_result = save_to_database(
                form.cleaned_data['name'],
                form.cleaned_data['url'],
                form.cleaned_data['interval_in_minutes']
                )
            
            if not save_to_database_result:
                messages.warning(request, 'Data was not saved because it already exists.')
            
            if save_to_database_result:
                process_form_data(form.cleaned_data['url'])
                
                
            form = RatingForm()  
    else:
        form = RatingForm()
    return render(request, 'rating.html', {'form': form})