import os#from x_forms.models import User#de preference importer toutes les tables pour generer les vues
import pathlib

from . import forms
from basic_app.models import User#de preference importer toutes les tables pour generer les vues
from basic_app.forms import UserProfileInfoForm,UserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

def curr_folder():
	chemin=str(pathlib.Path(os.path.dirname(os.path.abspath(__file__)))).split('/')
	curr_folder='/'+chemin[-1]+'/'
	return curr_folder
# Returns a Pathlib object
#print(curr_folder())
def index(request):
    return render(request, 'basic_app/index.html')
def other(request):
    return render(request, 'basic_app/other.html')
def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
# def form_name_view(request):#Rendu de la page avec la forme: doit contenir:
#     #etre sure que il y a une form:
#     t_form=forms.FormName()
#
#     if request.method=='POST':#si il s'agit d'une methode post, alors:
#         t_form=forms.FormName(request.POST)
#
#         if t_form.is_valid():
#             print("DATA Validated, here is the data provided")
#             print("email adress: "+t_form.cleaned_data['email'])
#             t_form.save(commit=True)
#             return index(request)#redirect to index page if form completed
#
#     return render(request, 'basic_app/registration.html', {'t_form':t_form})
            #return page_principale(request)#redirect to index page
def register(request):
	registered=False###key
	if request.method=='POST':
		user_form=UserForm(data=request.POST)###key
		profile_form=UserProfileInfoForm(data=request.POST)###key
		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)#hashing the password with set_password method
			user.save()

			profile = profile_form.save(commit=False)
			profile.user=user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']
			profile.save()
			registered=True
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form=UserForm()
		profile_form=UserProfileInfoForm()
		# on doit passer les )###key: user_form,profile_form et registered en dictionnary vers la view
	return render(request, 'basic_app/signup.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})

# decorateur a placer avant la fonction pour dire que ce nest actif que si condition passee:
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
def user_login(request):
	# if user has filled in the login information in login.html:
	if request.method=='POST':
		# Get the username and password suplied in the inputs of login.html
		username=request.POST.get('username')
		password=request.POST.get('password')
		# now we use django authentication tool to authenticate the user
		user=authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse('Account not Active')
		else:
			print('Username: {} and password: {}'.format(username,password))
			return HttpResponse(reverse('Invalid Account'))
	else:
		return render(request, 'basic_app/login.html',{})
