from django.test import TestCase
import os

class NotifyConfigTest(TestCase):
    def test_temp(self):
        print(os.environ.get('SECRET_KEY'))