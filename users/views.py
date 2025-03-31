from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from mainapp.models import Listing
from .forms import UserForm,ProfileForm,LocationForm
def login_view(request):
    if request.method=='POST':
        login_form=AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data.get('username')
            password=login_form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f'you are now logged in as {username}')
                return redirect('home')
            else:
                messages.error(request,f'An error occured')
            print(user)
        else:
            messages.error(request,f'An error occured')

    elif request.method=='GET':
        login_form=AuthenticationForm()
    return render(request,'views/login.html',{'login_form':login_form})

#logout function
@login_required
def logout_view(request):
    logout(request)
    messages.info(request,'You are now logged out')
    return redirect('mainpage')




# def register_view(request):
#     register_form=UserCreationForm()
#     return render(request,'views/register.html',{'register_form':register_form})


class RegisterView(View):
    def get(self,request):
        register_form=UserCreationForm()
        return render(request,'views/register.html',{'register_form':register_form})
    
    def post(self,request):
        register_form=UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user=register_form.save()
            user.refresh_from_db()
            login(request,user)
            messages.success(request,f'User {user.username} registered Successfully')
            return redirect('home')
        else:
            messages.error(request,f'An error occured trying to register')
            return render(request,'views/register.html',{'register_form':register_form})
        
@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    
    def get(self,request):
        user_listing=Listing.objects.filter(seller=request.user.profile)
        user_form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=request.user.profile)
        location_form=LocationForm(instance=request.user.profile.location)
        return render(request,'views/profile.html',{'user_form':user_form,'profile_form':profile_form,'location_form':location_form,'user_listing':user_listing})
    
    def post(self,request):
        user_form=UserForm(request.POST, instance=request.user)
        profile_form=ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        location_form=LocationForm(request.POST, instance=request.user.profile.location)
        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            messages.success(request,'Profile updated successfully')
            return redirect('home')
        else:
            messages.error(request,'An error occured')
            return render(request,'views/profile.html',{'user_form':user_form,'profile_form':profile_form,'location_form':location_form})



