from django.shortcuts import render, get_object_or_404, redirect
from .models import *
#from .forms import NewUserForm
from django.contrib.auth import login,logout 
from django.contrib import messages
from .forms import RegisterForm

def home(request):
    return render(request, 'home.html')

def Gym_exercise(request):
    gexercises = GExercise.objects.all()
    return render(request, 'gym_exercises.html', {'gexercises': gexercises})

def exercise_detail(request, pk):
    exercise = get_object_or_404(GExercise, pk=pk)
    return render(request, 'exercise_detail.html', {'exercise': exercise})

def Home_exercises(request):
    hexercises = HExercise.objects.all()
    return render(request, 'Home_exercises.html', {'hexercises': hexercises})

def yoga(request):
    yexercises = Yoga.objects.all()
    return render(request, 'yoga.html', {'yexercises': yexercises})

def stretch(request):
    s_exercises = S_Exercise.objects.all()
    return render(request, 'stretch.html', {'s_exercises': s_exercises})

def pt(request):
    pt_exercises = pt_Exercises.objects.all()
    return render(request, 'pt.html', {'s_exercises': pt_exercises})


def exercise_create(request):
    if request.method == 'POST':
        # create new exercise based on form data
        pass
    else:
        # display form to create new exercise
        pass


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('home.html')



from .forms import ExerciseForm
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ExerciseForm

def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('gym_exercises'))
    else:
        form = ExerciseForm()

    return render(request, 'exercise_create.html', {'form': form})

def contact(request):
    contact=Contact.objects.all()
    return render(request, 'contact.html')

def membership(request):
    membership=Membership.objects.all()
    return render(request, 'membership.html')

#def checkout(request):
 #   checkout=Checkout.objects.all()
  #  return render(request, 'checkout.html')



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import AddToCartForm

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            # process the form data
            quantity = form.cleaned_data['quantity']
            # add the product to the cart
            # redirect to the cart page
            messages.success(request, f"{product.name} added to cart.")
            return redirect('cart')
    else:
        form = AddToCartForm()
    context = {
        'product': product,
        'form': form
    }
    return render(request, 'add_to_cart.html', context)
