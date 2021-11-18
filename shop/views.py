
from django.shortcuts import render, redirect
from .forms import NewUserForm, UpdateUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'shop/home.html',
                  {'shop': home})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("shop:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/registration.html", context={"register_form": form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='/')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'registration/profile.html', {'user_form': user_form})

