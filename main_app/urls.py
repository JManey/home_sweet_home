from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup', views.signup, name='signup'),
  path('properties/', views.properties_index, name='index'),
  path('properties/create/', views.PropertyCreate.as_view(), name='properties_create'),
  path('properties/<int:pk>/update/', views.PropertyUpdate.as_view(), name='properties_update'),
  path('properties/<int:property_id>/', views.properties_detail, name='detail'),
  path('properties/<int:property_id>/update/', views.PropertyUpdate.as_view(), name='properties_update'),
  path('properties/<int:pk>/delete/', views.PropertyDelete.as_view(), name='properties_delete'),
  #AGENTS ROUTE
  path('agents/', views.agents_index, name='agents_index'),
  path('agents/<int:agent_id>/', views.agents_details, name='agents_details'),
  # add photo url
  path('properties/<int:property_id>/add_photo/', views.add_photo, name='add_photo'),
  path('users/<int:agent_id>/add_photo_user/', views.add_photo_user, name='add_photo_user'),
  ]