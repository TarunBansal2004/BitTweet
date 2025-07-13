from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def other(request):
    return render(request, 'other.html')

@login_required
def timeline(request):
    edit_tweet = None
    
    # Check if we're editing a tweet
    edit_tweet_id = request.GET.get('edit')
    if edit_tweet_id:
        edit_tweet = get_object_or_404(Tweet, pk=edit_tweet_id, user=request.user)
    
    if request.method == 'POST':
        if edit_tweet:
            # Handle tweet editing
            form = TweetForm(request.POST, request.FILES, instance=edit_tweet)
            if form.is_valid():
                form.save()
                return redirect('timeline')
        else:
            # Handle tweet creation
            form = TweetForm(request.POST, request.FILES)
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect('timeline')
    else:
        if edit_tweet:
            form = TweetForm(instance=edit_tweet)
        else:
            form = TweetForm()
    
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'timeline.html', {
        'tweets': tweets, 
        'form': form, 
        'edit_tweet': edit_tweet
    })



@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('timeline')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})