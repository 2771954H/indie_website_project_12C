from django.contrib.auth.backends import BaseBackend
from indie.models import UserProfile
from django.contrib.auth.models import User

#Dev login
class DevBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            dev = User.objects.get(username = username)
            user = dev.user
        except UserProfile.DoesNotExist:
            return None
        
        if not dev.is_dev:
            return None
        
        return dev
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk = user_id)
        except User.DoesNotExist:
            return None