from django.contrib.auth import get_user_model
 
User = get_user_model()
 
random_ = User.objects.last()

# my follower
random_.profile.followers.all()

# Who i follow

random_.is_following.all() # == random_.profile.following.all()