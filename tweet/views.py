from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Tweet

# Create your views here.
def home(request):
  tweet = Tweet.objects.all().order_by('-created_at')
  return render (request,'tweet/home.html',{'tweets':tweet})

@login_required
def make_tweet(request):
  if request.method == 'POST':
    text = request.POST.get('text')

    photo = request.FILES.get('photo')

    Tweet.objects.create(
      user = request.user,
      text = text,
      photo = photo
    )
    return redirect('home')
  return render(request,'tweet/make_tweet.html')
