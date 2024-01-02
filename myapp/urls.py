from django.urls import path
from myapp.views import register_user, registration_success

urlpatterns = [
    # Other URL patterns
    path('register/', register_user, name='register'),
    path('registration-success/', registration_success, name='registration_success'),  # This should match the redirect name
    # Define a URL for the registration success page
]
