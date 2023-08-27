from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
import stripe

class StripeCheckoutViewTest(APITestCase):

    @patch('stripe.checkout.Session.create')
    def test_successful_checkout(self, mock_create_session):
        # Mock Stripe API response
        mock_create_session.return_value = {
            'id': 'test_session_id',
            'url': 'https://example.com/session/test_session_id',
        }

        url = reverse('stripe-checkout')
        response = self.client.post(url)

        print(response.content)  # Print the response content for debugging

        # Check that the response status is 302 (redirect)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        # Check that the response redirected to the expected URL
        self.assertEqual(response.url, 'https://example.com/session/test_session_id')


    @patch('stripe.checkout.Session.create')
    def test_failed_checkout(self, mock_create_session):
        # Mock Stripe API response for a failed checkout
        mock_create_session.side_effect = stripe.error.StripeError(message='Stripe API error')

        url = reverse('stripe-checkout')
        response = self.client.post(url)

        # Check that the response status is 500 (internal server error)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], 'Sorry, something went wrong!')
