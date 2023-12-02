from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.forms import UserRegistrationForm,UserEditForm,ProfileEditForm
from .models import Profile
from django.contrib import messages

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.success(request,'Account Created Successfully')
            return render(request,'account/register_done.html',{'new_user':new_user})
        else:
            messages.error(request,'Error Creating Your Account')
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form':user_form})

@login_required
def edit(request):
    if request.method=='POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile Updated Successfully')
        else:
            messages.error(request,'Error Updating Your Profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form})