from django.test import TestCase
from .models import UserKYC, ConsentReceipt

class UserKYCModelTest(TestCase):
    def setUp(self):
        self.user_kyc = UserKYC.objects.create(
            name="John Doe",
            aadhaar_number="1234-5678-9012",
            pan_number="ABCDE1234F",
            selfie="path/to/selfie.jpg"
        )

    def test_user_kyc_creation(self):
        self.assertEqual(self.user_kyc.name, "John Doe")
        self.assertEqual(self.user_kyc.aadhaar_number, "1234-5678-9012")
        self.assertEqual(self.user_kyc.pan_number, "ABCDE1234F")

class ConsentReceiptModelTest(TestCase):
    def setUp(self):
        self.consent_receipt = ConsentReceipt.objects.create(
            user=self.user_kyc,
            consent_granted=True
        )

    def test_consent_receipt_creation(self):
        self.assertTrue(self.consent_receipt.consent_granted)
        self.assertEqual(self.consent_receipt.user, self.user_kyc)