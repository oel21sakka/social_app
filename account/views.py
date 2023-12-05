from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.forms import UserRegistrationForm,UserEditForm,ProfileEditForm
from .models import Profile, Follow
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

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


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user/list.html', {'section':'people', 'users':users})

@login_required
def user_detail(request,username):
    user = get_object_or_404(User,username=username)
    return render(request, 'user/detail.html', {'section':'people','user':user})

@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Follow.objects.get_or_create(follower=request.user,followed=user)
            else:
                Follow.objects.filter(follower=request.user,followed=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'error'})
    return JsonResponse({'status':'error'})