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
    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(request.POST, instance=user)
        profile_form = Staff_form(request.POST or None, request.FILES or None, instanceuser.profile)
        if user_form.is_valid()  and profile_form.is_valid():
            user_form.save()
            profile_form.save()


            if profile_form.cleaned_data["staff"]:
                user.is_staff = True
                user.save()
            else:
                user.is_staff = False
                user.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return myProfile(request, user_id)
       


    
    else:
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(instance=user)
        profile_form = Staff_form(instance=user.profile)
    
    return render(request, 'userapp/user_edit_profile_form.html',{'user_form': user_form, 'profile_form': profile_form})

        




def deactivatemyProfile(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_active:
        user.is_active = False
        user.save()
    else:
        user.is_staff = True
        user.save()
    messages.success(request, ('Your profile was successfully updated!'))
    return myProfile(request, user_id)
        

@login_required
def manageStaff(request):
    staff = profile.objects.all().filter(is_staff=True)
    return render(request=request, template_name="userapp/display_staff.html",content_type={"staff_detail":staff})

@login_required
def manageCustomer(request, user_id):
      staff = profile.objects.all().filter(is_staff=False)
      return render(request=request, template_name="userapp/display_customer.html",content_type={"customer":staff})
