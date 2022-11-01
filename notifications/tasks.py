import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from notifications.models import UserSubscription


@shared_task()
def fetch_daily_summary():
    response = requests.get(url="http://host.docker.internal:8001/news/daily-summary/")
    if response.headers.get("content-type") != "application/json":
        return "FAILURE"
    daily_summary = response.json()
    subscriptions = UserSubscription.objects.filter(active=True)
    for ticker_news in daily_summary:
        ticker = ticker_news.get("ticker")
        news = ticker_news.get("news")
        if not ticker:
            continue
        subject = f"Daily summary regarding {ticker}"
        recipient_list = list(subscriptions.filter(ticker=ticker, active=True).values_list("email", flat=True))
        if news and recipient_list:
            send_mail(subject, news, settings.EMAIL_HOST_USER, recipient_list)
    return "SUCCESS"
