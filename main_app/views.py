from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Profile, Company, Property



def is_agent_check(user):
    return user.is_agent

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user'form object
    # that include the data form browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def properties_index(request):
  properties = Property.objects.all()
  return render(request, 'properties/index.html', {'properties': properties})

def properties_detail(request, property_id):
  property = Property.objects.get(id=property_id)
  
  return render(request, 'properties/detail.html', { 
    'property': property
  })

#below doesn't work on class based
# @user_passes_test(is_agent_check, login_url='/login/')


class PropertyCreate(UserPassesTestMixin, CreateView):
  def test_func(self):
    return self.request.user.profile.is_agent
  model = Property
  fields = ['street_address', 'city', 'state', 'beds', 'baths', 'price', 'sqft', 'levels', 'date_listed', 'status']

  def form_valid(self, form):
    # assign the logged in user self.request.user
    form.instance.user = self.request.user
    # let the createView do its usual task
    return super().form_valid(form)

class PropertyUpdate(LoginRequiredMixin, UpdateView):
  model = Property
  fields = ['street_address', 'city', 'state', 'beds', 'baths', 'price', 'sqft', 'levels', 'date_listed', 'status']

class PropertyDelete(LoginRequiredMixin, DeleteView):
  model = Property
  success_url = '/properties/'
