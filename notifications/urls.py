from django.urls import path

from .views import subscribe_to_ticker, unsubscribe_from_ticker

urlpatterns = [
    path('subscribe/', subscribe_to_ticker, name="subscribe"),
    path('unsubscribe/', unsubscribe_from_ticker, name="unsubscribe")
]
