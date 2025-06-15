from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from authentication.forms import RegistrationForm
from directory.models import Profile

@csrf_protect
def register_user_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            user.save()

            Profile.objects.create(
                user=user,
                user_type=form.cleaned_data['user_type'],
                profile_picture=form.cleaned_data['profile_picture'],
                address_line1=form.cleaned_data['address_line1'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode']
            )
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Error creating account. Please correct the form.')
    else:
        form = RegistrationForm()
    
    context = {
        'form': form        
    }

    return render(request, 'directory/registration.html', context)

@csrf_protect
def login_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")

            user_type = user.profile.user_type
            if user_type == 'doctor':
                return redirect('doctor-dashboard')
            elif user_type == 'patient':
                return redirect('patient-dashboard')
            else:
                return redirect('login-page')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login-page')
    else:
        return render(request, 'directory/login.html')

@csrf_protect
def logout_user(request):
    logout(request)
    return redirect('login-page')

@login_required
def doctor_dashboard(request):
    return render(request, 'core/doctor_dashboard.html', {
        'user': request.user,
        'profile': request.user.profile
    })

@login_required
def patient_dashboard(request):
    return render(request, 'core/patient_dashboard.html', {
        'user': request.user,
        'profile': request.user.profile
    })
