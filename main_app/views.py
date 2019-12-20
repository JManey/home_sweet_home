<<<<<<< HEAD
from django.shortcuts import render
=======
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
>>>>>>> master
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
<<<<<<< HEAD
=======
from .models import Profile, Company, Property

>>>>>>> master

# Create your views here.
def home(request):
  return render(request, 'home.html')

<<<<<<< HEAD
=======
def about(request):
  return render(request, 'about.html')
>>>>>>> master

def signup(request):
  error_message = ''
  if request.method == 'POST':
<<<<<<< HEAD
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
=======
    # This is how to create a 'user'form object
    # that include the data form browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - please try again'
>>>>>>> master
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

<<<<<<< HEAD

# @login_required

# class ClassName(   LoginRequiredMixin,       OtherStuff, OtherStuff):
=======
def properties_index(request):
  properties = Property.objects.all()
  return render(request, 'properties/index.html', {'properties': properties})

def properties_detail(request, property_id):
  property = Property.objects.get(id=property_id)
  
  return render(request, 'properties/detail.html', { 
    'property': property
  })

class PropertyCreate(LoginRequiredMixin, CreateView):
  model = Property
  fields = ['street_address', 'city', 'state', 'beds', 'baths', 'price', 'sqft', 'levels', 'date_listed', 'status']

  def form_valid(self, form):
    # assign the logged in user self.request.user
    form.instance.user = self.request.user
    # let the createView do its usual task
    return super().form_valid(form)

class PropertyUpdate(LoginRequiredMixin, UpdateView):
  model = Property
  fields = '__all__'
>>>>>>> master
