from django.shortcuts import render

# Create your views here.
def dream(request):
    return render(request, "dream.html")

def dream2(request):
    return render(request, "dream2.html")