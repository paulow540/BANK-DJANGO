from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm, User_form, Staff_form
from django.contrib.auth.models import User

from .models import profile
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
# from django.contrib.auth.decorators import login_required

# Create your views here.


class  SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




@login_required
def myProfile(request, user_id):
    my_profile = profile.objects.all().filter(user_id=user_id)

    return render(request, "userapp/my_profile.html", {"my_profile": my_profile})



@login_required
@transaction.atomic
def editmyProfile(request, user_id):
    if request.method = "POST":
        pass
    
    else:
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(instance=user)
        profile_form = Staff_form(instance=user.profile)
    
    return render(request, 'userapp/user_edit_profile_form.html',{'user_form': user_form, 'profile_form': profile_form})

        




def deactivatemyProfile(request, user_id):
    return 0

@login_required
def manageStaff(request, user_id):
    pass

@login_required
def manageCustomer(request, user_id):
    pass