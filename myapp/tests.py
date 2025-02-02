from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question_en="Test question",
            answer_en="<p>Test answer</p>"
        )
        self.client = APIClient()

    def test_model_translation(self):
        """Test automatic translation creation"""
        self.assertNotEqual(self.faq.question_hi, '')
        self.assertNotEqual(self.faq.answer_bn, '')

    def test_api_response(self):
        """Test API endpoint with language parameter"""
        response = self.client.get(reverse('faq-list') + '?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertIn('question', response.data[0])