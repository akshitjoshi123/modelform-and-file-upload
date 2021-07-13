from appFileUpload.models import Document
from django.shortcuts import render,redirect
from appFileUpload.forms import DocumentForm

# Create your views here.
def fileUp(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show/')
    else:
        form = DocumentForm()
    return render(request, 'index.html', {
        'form': form
    })

def show(request):
    obj = Document.objects.all()
    return render(request, 'show.html', {'obj':obj})