from django.contrib import admin # type: ignore
from .models import Profile, Post, LikePost, FollowersCount

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)