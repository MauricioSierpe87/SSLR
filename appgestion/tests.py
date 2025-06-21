from django.test import TestCase
from django.test import TestCase
from appgestion.models import CustomUser

class AdminTests(TestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create(
            username='test_admin',
            password='testpass123',
            is_data_admin=True
        )
    
    def test_admin_access(self):
        self.assertTrue(self.admin.is_data_admin)
# Create your tests here.
