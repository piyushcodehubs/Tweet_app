from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import TweetForms , UserRegistrationForm
from .models import Tweet
from django.contrib.auth import login


# Create your views here.
def home(request):
  tweet = Tweet.objects.all().order_by('-created_at')
  return render (request,'tweet/home.html',{'tweets':tweet})

@login_required
def make_tweet(request):
  if request.method =='POST':
    form =TweetForms(request.POST,request.FILES)
    if form.is_valid():
      tweet = form.save(commit=False)
      tweet.user = request.user
      tweet.save()
      return redirect('home')

  else:
    form = TweetForms()
  return render(request,'tweet/make_tweet.html', {'form':form})

@login_required
def tweet_edit(request,tweet_id):
  tweet = get_object_or_404(Tweet,pk= tweet_id, user = request.user)
  if request.method == 'POST':
    form = TweetForms(request.POST,request.FILES,instance=tweet)
    if form.is_valid():
      tweet=form.save(commit=False)
      tweet.user = request.user
      tweet.save()
      return redirect('home')
  else:
    form  = TweetForms(instance=tweet)
  return render(request,'tweet/make_tweet.html',{'form':form})

@login_required
def tweet_delete(request,tweet_id):
  tweet = get_object_or_404(Tweet,pk = tweet_id,user=request.user)
  if request.method =='POST':
    tweet.delete()
    return redirect('home')
  return render(request,'tweet/tweet_delete.html',{'tweet':tweet})



def register(request):
  if request.method == 'POST':
    form=UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request,user)
      return redirect('home')
  else:
    form = UserRegistrationForm()
  return render(request,'registration/register.html',{'form':form})


