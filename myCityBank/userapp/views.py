from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from .models import profile
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction

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
    return 0


def deactivatemyProfile(request, user_id):
    return 0

@login_required
def manageStaff(request, user_id):
    pass

@login_required
def manageCustomer(request, user_id):
    pass