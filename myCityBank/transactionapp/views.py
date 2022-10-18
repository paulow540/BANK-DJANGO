from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def manageAccount(request):
    staff = profile.objects.all().filter(is_staff=True)
    return render(request=request, template_name="userapp/display_staff.html",content_type={"staff_detail":staff})
