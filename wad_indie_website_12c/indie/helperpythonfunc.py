from indie.models import UserProfile

#Checks if the current logged in user is a dev- put in every dev page
def check_dev(request):
    profile = get_current_profile(request)
    if profile.is_dev == False:
        return index(request)
    

def get_current_profile(request):
    profile = UserProfile.object.get(user= request.user)