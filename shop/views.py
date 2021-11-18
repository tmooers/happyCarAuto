from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.views import generic
from cart.forms import CartAddProductForm


now = timezone.now()


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


class ProductListView(generic.ListView):
    model = Part

class CategorylistView(generic.ListView):
    model = PartType

class category_detail(generic.DetailView):
    model = PartType

def product_detail(request, id):
    product=get_object_or_404(Part,id=id,availability=True)
    cart_part_form = CartAddProductForm()
    return render(request,'shop/part/detail.html',{'part':product,'cart_part_form':cart_part_form})
