from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     bio = models.TextField(max_length=500, blank=True, null=True)
#     birthday = models.DateField(blank=True, null=True)
#     location = models.CharField(max_length=100, blank=True, null=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# def __str__(self):
#         return f"{self.user.username}'s Profile"

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    photo = models.ImageField(upload_to='tweets/', blank=True, null=True)
    mood = models.CharField(max_length=20, choices=[('Happy', 'Happy'), ('Sad', 'Sad'), ('Nostalgic', 'Nostalgic')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def  __str__(self):
    return f"{self.user.username} - {self.text[:10]}"