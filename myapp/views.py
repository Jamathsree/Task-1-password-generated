from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.shortcuts import render

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # You can access the generated password via the user object if needed
            generated_password = user.password  # Not recommended to access the password directly for security reasons

            # You might want to send the generated password to the user's email
            # Add email sending functionality here
            # You can use Django's email functionality or a third-party library like SendGrid or SMTP

            return redirect('registration_success')  # Redirect to a success page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration_form.html', {'form': form})


def registration_success(request):
    return render(request, 'registration_success.html')
