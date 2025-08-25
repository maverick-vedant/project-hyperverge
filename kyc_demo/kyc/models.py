from django.db import models

class UserKYC(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    aadhaar_number = models.CharField(max_length=12, unique=True)
    pan_number = models.CharField(max_length=10, unique=True)
    selfie = models.ImageField(upload_to='selfies/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ConsentReceipt(models.Model):
    user_kyc = models.ForeignKey(UserKYC, on_delete=models.CASCADE)
    consent_given = models.BooleanField(default=False)
    consent_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Consent for {self.user_kyc.name} - {"Granted" if self.consent_given else "Denied"}'