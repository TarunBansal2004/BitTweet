from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request , 'index.html')

def other(request):
    return render(request, 'other.html')

def timeline(request):
   tweets =  Tweet.objects.all().order_by('-created_at')
   return render(request , 'timeline.html' , {'tweets':tweets})

def tweet_list(request):
    Tweet.object.all().order_by('-created_at')

def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('timeline')
        pass
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})