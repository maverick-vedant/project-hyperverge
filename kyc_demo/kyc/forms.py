from django import forms

class DocumentUploadForm(forms.Form):
    document_type = forms.ChoiceField(choices=[
        ('aadhaar', 'Aadhaar'),
        ('pan', 'PAN'),
    ])
    document_file = forms.FileField()

class ConsentForm(forms.Form):
    consent_given = forms.BooleanField(required=True, label="I give my consent for KYC processing.")

class KYCForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    document = forms.FileField()
    consent = forms.BooleanField(required=True, label="I agree to the terms and conditions.")
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field    