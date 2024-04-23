from django.shortcuts import render
from django.contrib import messages
from .forms import RatingForm
from .utils import save_to_database
from .models import RatingRecord, LinkSetting
import matplotlib.pyplot as plt
import base64
from io import BytesIO

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
                0
                # form.cleaned_data['interval_in_minutes']
                )
            
            if not save_to_database_result:
                messages.warning(request, 'Data was not saved because it already exists.')
                
            form = RatingForm()  
    else:
        form = RatingForm()
    return render(request, 'rating.html', {'form': form})

def link_setting_list_view(request):
    link_settings = LinkSetting.objects.all()
    return render(request, 'link_setting_list.html', {'link_settings': link_settings})

def link_setting_edit_view(request):
    return render(request, 'link_setting_edit.html')

def graph_result_view(request):
    link_settings = LinkSetting.objects.all()
    selected_name = request.GET.get('link_setting_name')  # Get selected link setting name from request
        
    if selected_name:
        rating_records = RatingRecord.objects.filter(link_setting__name=selected_name)
    else:
        rating_records = RatingRecord.objects.all()
        
    # Prepare data for plotting
    time = [record.created_at for record in rating_records]
    rating_values = [record.rating_value for record in rating_records]
    review_counts = [record.review_count for record in rating_records]
    
    # Graph 1: Time vs Rating Value
    plt.figure(figsize=(10, 5))
    plt.plot(time, rating_values)
    plt.xlabel('Time')
    plt.ylabel('Rating')
    plt.title('Time vs Rating')
    # Save the plot to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph1_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Graph 2: Time vs Review Count
    plt.figure(figsize=(10, 5))
    plt.plot(time, review_counts)
    plt.xlabel('Time')
    plt.ylabel('Review Count')
    plt.title('Time vs Review Count')
    # Save the plot to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph2_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    
    return render(request, 'graph_result.html', {'link_settings': link_settings, 'selected_name': selected_name, 'graph1_image': graph1_image, 'graph2_image': graph2_image})

def table_result_view(request):
    rating_records = RatingRecord.objects.all()
    return render(request, 'table_result.html', {'rating_records': rating_records})