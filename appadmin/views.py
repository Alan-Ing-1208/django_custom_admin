from django.contrib.auth.models import User
from .models import Payment
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserForm


def api_stats(request):
    values = list(Payment.objects.order_by('-timestamp').values_list('amount', flat=True)[:5])
    return JsonResponse({'values': values[::-1]})


def home_view(request):
    return HttpResponse("Welcome to the custom Django Admin!")


@staff_member_required
def custom_admin_dashboard(request):
    user_count = User.objects.count()
    total_payments = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    recent_users = User.objects.order_by('-date_joined')[:5]

    return render(request, 'admin/index.html', {
        'user_count': user_count,
        'total_payments': total_payments,
        'recent_users': recent_users,
    })


def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("login")  # Redirect to login page
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserForm()

    return render(request, 'registration/register.html', {'form': form})  # Render register.html


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("custom_admin_dashboard")  # Redirect to dashboard
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})  # Render login.html


def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout


@login_required
def custom_admin_dashboard(request):
    return render(request, 'admin/custom_admin_dashboard.html')