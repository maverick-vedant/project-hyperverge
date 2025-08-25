from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import KYCForm

def kyc_home(request):
    return render(request, 'kyc/home.html')

def kyc_form_view(request):
    if request.method == 'POST':
        form = KYCForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            # Save the KYC data to the database or perform other actions
            return redirect('kyc_success')
    else:
        form = KYCForm()
    return render(request, 'kyc/kyc_form.html', {'form': form})

def kyc_success(request):
    return render(request, 'kyc/kyc_success.html')