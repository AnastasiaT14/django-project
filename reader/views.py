from django.shortcuts import render
from forms import ReaderForm
def reader(request):
    return render(request, 'reader.html', {"form": ReaderForm})
