from pyexpat.errors import messages
from django.shortcuts import redirect, render

from portfolio.forms import PortfolioForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Message was successfully Sent')
            return redirect('index')
        else:
            return render(request, 'contact.html', {'form': form, 'errors': form.errors})
    else:
        form = PortfolioForm()
    return render(request, 'contact.html', {'form': form})
