from django.shortcuts import render
from .models import Reviews
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'review/index.html')

@csrf_exempt
def save_review(request):
    result = Reviews().save_reviews(request.POST['rating'],request.POST['reviews'])
    context={'result':result}
    return render(request, 'review/confirmation.html',context)


@csrf_exempt
def allreviews(request):
    """The home page for Learning Log"""
    reviews = Reviews().get_reviews()
    context={'reviews':reviews}
    return render(request, 'review/allreviews.html',context)