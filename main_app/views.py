from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import operator, uuid, boto3
from django.db.models import Q
from .models import Profile, Company, Property, Photo

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'property-photos-hsh'

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


# filterable index
def properties_index(request):
  qs = Property.objects.all()
  # print('************', qs[2].photo_set.all)
  city = request.GET.get('city')
  state = request.GET.get('state')
  beds = request.GET.get('beds')
  baths = request.GET.get('baths')
  min_price = request.GET.get('min_price')
  max_price = request.GET.get('max_price')
  min_sqft = request.GET.get('min_sqft')
  max_sqft = request.GET.get('max_sqft')
  levels = request.GET.get('levels')
  status = request.GET.get('status')

  if city != '' and city is not None:
    qs = qs.filter(city__icontains=city)
  if state != '' and state is not None:
    qs = qs.filter(state__icontains=state)
  if beds != '' and beds is not None:
    qs = qs.filter(beds__icontains=beds)
  if baths != '' and baths is not None:
    qs = qs.filter(baths__icontains=baths)
  if min_price != '' and min_price is not None:
    qs = qs.filter(price__gte=min_price)
  if max_price != '' and max_price is not None:
    qs = qs.filter(price__lte=max_price)
  if min_sqft != '' and min_sqft is not None:
    qs = qs.filter(sqft__gte=min_sqft)
  if max_sqft != '' and max_sqft is not None:
    qs = qs.filter(sqft__lte=max_sqft)
  if levels != '' and levels is not None:
    qs = qs.filter(levels=levels)
  if status != '' and status is not None:
    qs = qs.filter(status=status)

  if city == None:
    city = ''
  if state == None:
    state =''

  context = {
      'city': city,
      'state': state,
      'beds': beds,
      'baths': baths,
      'min_price': min_price,
      'max_price': max_price,
      'min_sqft': min_sqft,
      'max_sqft': max_sqft,
      'levels': levels,
      # 'status': status,
      'qs': qs,
  }

  return render(request, 'properties/index.html', context)



def properties_detail(request, property_id):
  property = Property.objects.get(id=property_id)
  return render(request, 'properties/detail.html', {
    'property': property
  })


#AGENTS LIST
def agents_index(request):
  # agents = User.objects.all()
  agents = Profile.objects.filter(is_agent=True)
  return render(request, 'agents/agents_index.html', {'agents': agents})
#AGENT SHOW PAGE
def agents_details(request, agent_id):
  agent = Profile.objects.get(id=agent_id)
  return render(request, 'agents/agents_details.html', {'agent': agent})


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

class PropertyUpdate(UserPassesTestMixin, UpdateView):
  def test_func(self):
    return self.request.user.profile.is_agent
  model = Property
  fields = ['street_address', 'city', 'state', 'beds', 'baths', 'price', 'sqft', 'levels', 'date_listed', 'status']

class PropertyDelete(UserPassesTestMixin, DeleteView):
  def test_func(self):
    return self.request.user.profile.is_agent
  model = Property
  success_url = '/properties/'

def add_photo(request, property_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, property_id=property_id)
      photo.save()
    except:
      print('An error occurred while uploading to AWS')
  return redirect('detail', property_id=property_id)