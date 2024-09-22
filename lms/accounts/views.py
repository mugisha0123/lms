from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from employee.models import *
from .forms import UserLoginForm,UserAddForm



def changepassword(request):
	if not request.user.is_authenticated:
		return redirect('/')
	'''
	Please work on me -> success & error messages & style templates
	'''
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save(commit=True)
			update_session_auth_hash(request,user)

			messages.success(request,'Password changed successfully',extra_tags = 'alert alert-success alert-dismissible show' )
			return redirect('accounts:changepassword')
		else:
			messages.error(request,'Error,changing password',extra_tags = 'alert alert-warning alert-dismissible show' )
			return redirect('accounts:changepassword')
			
	form = PasswordChangeForm(request.user)
	return render(request,'accounts/change_password_form.html',{'form':form})




def register_user_view(request):
	# WORK ON (MESSAGES AND UI) & extend with email field
	if request.method == 'POST':
		form = UserAddForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			username = form.cleaned_data.get("username")

			messages.success(request,'Account created successfully',extra_tags = 'alert alert-info' )
			return redirect('accounts:users')
		else:
			messages.error(request,'failed to create user',extra_tags = 'alert alert-warning alert-dismissible show')
			return redirect('accounts:register')


	form = UserAddForm()

	context = {
		"form":form,
	}
	return render(request,'accounts/register.html',context)




def login_view(request):
    # If the user is already authenticated, redirect to home
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")  # Inform the user they are already logged in
        return redirect("dashboard:dashboard")
        
    # If the request method is POST, process the form data
    if request.method == "POST":
        form = UserLoginForm(request.POST)  # Use your custom form
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"you have successfully logged In, {user.username}!")  # Success message
                return redirect("dashboard:dashboard")
            else:
                messages.error(request, "Invalid username or password.")  # Error message for failed authentication
        else:
            messages.error(request, "Please correct the errors below.")  # Error message for form validation failure
    else:
        form = UserLoginForm()  # Use your custom form
    
    # Render the login page with the form
    return render(request, "accounts/login.html", {"form": form})
    
    	


    
    
	# '''
	# work on me - needs messages and redirects
	
	# '''
	# login_user = request.user
	# if request.method == 'POST':
	# 	form = UserLogin(data = request.POST)
	# 	if form.is_valid():
	# 		username = request.POST.get('username')
	# 		password = request.POST.get('password')

	# 		user = authenticate(request, username = username, password = password)
	# 		if user and user.is_active:
	# 			login(request,user)
	# 			if login_user.is_authenticated:
	# 				return redirect('dashboard:dashboard')
	# 		else:
	# 			messages.error(request,'Account is invalid',extra_tags = 'alert alert-error alert-dismissible show' )
	# 			return redirect('accounts:login')

	# 	else:
	# 		return HttpResponse('data not valid')

	# dataset=dict()
	# form = UserLogin()

	# dataset['form'] = form
	# return render(request,'accounts/login2.html',dataset)




def user_profile_view(request):
	if not request.user.is_authenticated:
		return redirect("accounts:login")
	emp = getattr(request.user, 'employee', None)
	
	if emp:
		return render(request, 'accounts/user_profile_page.html',{"emp":emp})

	else:
		error_message = "You don't have any profile you may logout or contact you system admin."
		messages.warning(request, error_message)
		return redirect('dashboard:dashboard')
        

    




def logout_view(request):
	logout(request)
	return redirect('accounts:login')



def users_list(request):
	userz = User.objects.all()
	return render(request,'accounts/users_table.html',{'userz':userz,'title':'Users List'})


def users_unblock(request,id):
	user = get_object_or_404(User,id = id)
	emp = Employee.objects.filter(user = user).first()
	emp.is_blocked = False
	emp.save()
	user.is_active = True
	user.save()

	return redirect('dashboard:employees')


def users_block(request,id):
	user = get_object_or_404(User,id = id)
	emp = Employee.objects.filter(user = user).first()
	emp.is_blocked = True
	emp.save()
	
	user.is_active = False
	user.save()
	
	return redirect('dashboard:employees')



def users_blocked_list(request):
	blocked_employees = Employee.objects.all_blocked_employees()
	return render(request,'accounts/all_deleted_users.html',{'employees':blocked_employees,'title':'blocked users list'})