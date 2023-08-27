from django.conf import settings
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeCheckoutView(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1Njox8Jrd2Q2u0o6PJDUMDI3',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=settings.SITE_URL + '?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '?canceled=true',
            )

            return redirect(checkout_session.url)

        except:
            return Response(
                {'error': 'Sorry, something went wrong!'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

