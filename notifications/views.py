from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UserSubscription

ALLOWED_TICKERS = {"TSLA", "FB", "AMZN", "TWTR", "NFLX"}


def update_subscription_status(data, active):
    if not data:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    email, ticker = data.get("email"), data.get("ticker")
    if not email or ticker not in ALLOWED_TICKERS:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    _, created = UserSubscription.objects.update_or_create(email=email, ticker=ticker, defaults={"active": active})
    return Response(status=status.HTTP_201_CREATED) if created else Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def subscribe_to_ticker(request):
    return update_subscription_status(request.data, True)


@api_view(["POST"])
def unsubscribe_from_ticker(request):
    return update_subscription_status(request.data, False)
