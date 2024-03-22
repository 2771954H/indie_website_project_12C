from indie.models import UserProfile
from indie.views import index

#Helper functions
#Checks if the current logged in user is a dev- put in every dev page
def check_dev(request):
    profile = get_current_profile(request)
    if profile.__getattribute__('is_dev') == False:
        return index(request)
    

def get_current_profile(request):
    return UserProfile.objects.get(user = request.user)
