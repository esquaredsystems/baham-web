from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('', views.view_home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('baham/vehicles', views.view_vehicles, name='vehicles'),
    path('baham/vehicles/create', views.create_vehicle, name='createvehicle'),
    path('baham/vehicles/save/', views.save_vehicle, name='savevehicle'),
    path('baham/vehicles/delete/<str:uuid>', views.delete_vehicle, name='deletevehicle'),
    path('baham/vehicles/edit/<str:uuid>', views.edit_vehicle, name='editvehicle'),
    path('baham/vehicles/edit/update/', views.update_vehicle, name='updatedvehicle'),
    path('baham/aboutus', views.view_aboutus, name='aboutus'),
    
    ### REST API ###
    path('api/csrftoken', views.get_csrf_token, name='get_csrf_token'),
    path('api/get/vehiclemodels', views.get_all_vehicle_models, name='get_all_vehicle_models'),
    path('api/get/vehiclemodel/<str:uuid>', views.get_vehicle_model, name='get_vehicle_model'),
    path('api/create/vehiclemodel', views.create_vehicle_model, name='create_vehicle_model'),
    path('api/update/vehiclemodel/<str:uuid>', views.update_vehicle_model, name='update_vehicle_model'),
    path('api/delete/vehiclemodel/<str:uuid>', views.delete_vehicle_model, name='delete_vehicle_model'),
    
    
    ### USER PROFILE ###
    path('api/get/userprofiles', views.get_all_user_profiles, name='get_all_user_profiles'),
    path('api/get/userprofile/<str:uuid>', views.get_user_profile, name='get_user_profile'),
    path('api/create/userprofile', views.create_user_profile, name='create_user_profile'),
    path('api/update/userprofile/<str:uuid>', views.update_user_profile, name='update_user_profile'),
    path('api/delete/userprofile/<str:uuid>', views.delete_user_profile, name='delete_user_profile'),
]
