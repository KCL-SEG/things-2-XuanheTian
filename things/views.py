from django.shortcuts import render
from .forms import ThingForm
def home(request):
    form = ThingForm()
    return render(request, 'things/home.html', {'form': form})
