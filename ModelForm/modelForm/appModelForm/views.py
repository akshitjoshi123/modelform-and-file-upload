from django.shortcuts import render
from django.http import HttpResponse
from .forms import feedbackForm
from .models import feedback

# Create your views here.
def feedbackform(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            desc = form.cleaned_data['desc']
            obj = feedback(name=name, email=email, desc=desc)
            obj.save()
            context = {
                'name' : name,
                'email' : email,
                'desc' : desc
            }
            return render(request, "showdetails.html", context)
    else:
        form = feedbackForm()
    return render(request, 'index.html',{'form':form})
