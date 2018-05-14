from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
# from .forms import PostForm
# from .forms import RegistrationForm
from django.shortcuts import redirect
from .models import Post,VDetails
from django.contrib.auth import authenticate, login
# from django.urls import reverse_lazy
from django.core.mail import send_mail

from django.views import generic
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import (
    # RegistrationForm,
    EditProfileForm,
    TenderForm,
    CustomUserCreationForm,
    BirthCertificateForm
)
def home(request):
    posts = Post.objects.all
    return render(request,'grama/home.html',{'posts':posts})
@login_required
def index(request):
    return render(request,'citizen/index.html',{})
@login_required
def gindex(request):
    return render(request,'grama/index.html',{})
# def post_forms(request):
#     return render(request,'grama/forms.html')
def login(request):
    return render(request, 'grama/login.html',{})
def details(request):
    posts = Post.objects.all
    return render(request, 'grama/tenderdetails.html',{'posts': posts})

def logout(request):
    return render(request, 'grama/logout.html')

def service(request):
    return render(request,'grama/service.html')

# def register(request):
#     if request.method =='POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('/grama/login')
#             return redirect('/grama/login')
#         else:
#             # Do something in case if form is not valid
#             # raise Http404
#             return HttpResponseRedirect('/error/')
#     else:
#         form = RegistrationForm()
#
#         args = {'form': form}
#         return render(request, 'grama/reg_form.html', args)
def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            # messages.success(request, 'Account created successfully')
            return redirect('/login')

    else:
        f = CustomUserCreationForm()

    return render(request, 'grama/reg_form.html', {'form': f})

#
# def post_tender(request):
#         return render(request, 'grama/forms.html', {})
@login_required
def view_profile(request, pk=None):
    # # args = {'user': request.user}
    # user = request.user
    user = request.user
    #       # return render(request, 'grama/profile.html', args)
    # if user.is_superuser or user.is_staff:
    #     return redirect('/admin/')  # or your url name
    # else:
    #      return render(request, 'grama/profile/',request.user)

    if  user.is_superuser or user.is_staff:

        return redirect('/admin/')
    # elif request.user=='president':
    #     user = request.user
    #     args = {'user': user}
    #     return render(request, 'grama/profilep.html', args)
    # elif request.user=='vicepresident':
    #     args = {'user': user}
    #     return render(request, 'grama/profilevp.html', args)
    else:
        if request.user.username=='president':
            user = request.user
            posts = Post.objects.all
            vdetails=VDetails.objects.all
            args = {'user': user,'posts':posts,'vdetails':vdetails}
            return render(request, 'president/indexp.html', args)
        elif request.user.username=='vp':
            user = request.user
            args = {'user': user}
            return render(request, 'vicepresident/indexvp.html', args)
        elif request.user.username=='va':
            user = request.user
            args = {'user': user}
            return render(request, 'villageaccountant/indexva.html', args)
        elif request.user.username=='mem1'or request.user.username=='mem2'or request.user.username=='mem3'or request.user.username=='mem4':
            user = request.user
            args = {'user': user}
            return render(request, 'members/indexmb.html', args)
        else:
            user = request.user
            args = {'user': user}
            return render(request, 'citizen/index.html', args)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/grama/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'grama/edit_profile.html', args)
@login_required
def password_change(request):
    if request.method == 'POST':
        f = PasswordChangeForm(data=request.POST, user=request.user)

        if f.is_valid():
            f.save()
            update_session_auth_hash( request, f.user)
            return redirect('/grama/profile')
        else:
            return redirect('/grama/password_change')
    else:
        f = PasswordChangeForm(user=request.user)
        args = {'form': f}
        return render(request, 'grama/change_password.html', args)
# Tender Submission

def post_list(request):
    posts = Post.objects.all
    return render(request, 'grama/post-list.html', {'posts': posts})
# thank you
def thanks(request):
    return render(request, 'grama/respond.html',{})

def error(request):
    return render(request, 'grama/error.html')

    #this is submitting the tender form
# def post_tender(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = TenderForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...title	description	submitted_at	posted_on	Due_date	EMD	DOC_Fee	Notice_Type	Authority_Type	Product_Services	Doc_Sale_Starts	Doc_Sale_Ends	Doc_Submit_
#             # redirect to a new URL:
#             title= form.cleaned_data['title']
#             description = form.cleaned_data['description']
#             submitted by = form.cleaned_data['submitted_at']
#             posted on = form.cleaned_data['']
#             recipients = ['anizamuddin35@gmail.com']
#             if cc_myself:
#                 recipients.append(sender)
#
#             send_mail(subject, message, sender, recipients)
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = TenderForm()
#
#     return render(request, 'grama/forms.html', {'form': form})

# def post_tender(request):
#     if request.method =='POST':
#         form = TenderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('/grama/login')
#             return redirect('/grama/thanks')
#         else:
#             # Do something in case if form is not valid
#             raise Http404     # return HttpResponseRedirect('/')
#     else:
#         form = TenderForm()
#
#         args = {'form': form}
#         return render(request, 'grama/forms.html', args)

def post_tender(request):
    if request.method == 'POST':
        f = TenderForm(request.POST)
        if f.is_valid():
            f.save()
            # messages.success(request, 'Account created successfully')
            return redirect('/grama/thanks')

    else:
        f = TenderForm()

    return render(request, 'grama/forms.html', {'form': f})

#birth BirthCertificate
@login_required
def birth(request):
    if request.method == 'POST':
        f = BirthCertificateForm(request.POST)
        if f.is_valid():
            f.save()
            # messages.success(request, 'Account created successfully')
            return redirect('/grama/profile')

    else:
        f = BirthCertificateForm()

    return render(request, 'citizen/bforms.html', {'form': f})
