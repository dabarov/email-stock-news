# Stock Market News Emailing Microservice

## Installation

1. Clone this repo
2. Create `.env` file with the following keys:

```
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
SECRET_KEY=
DEBUG=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

Where `POSTGRES_***` is a values for db initialization and connection to it.
`SECRET_KEY` is a django secret key. `DEBUG` is a debug status of the project.
`EMAIL_HOST_USER` is an email from which the newsletters will be sent and authorized application password for this email
should be added as `EMAIL_HOST_PASSWORD`.

3. Run the following command to initialize the database via applying migrations.

```shell
docker compose run api python manage.py migrate
```

4. Start the app with the following command:

```shell
docker compose up
```

## Usage

- You can subscribe and unsubscribe user to a ticker using following endpoints:

```shell
http://localhost:8002/notifications/subscribe/
http://localhost:8002/notifications/unsubscribe/
```

The body of the post request to these endpoints should include `email` of the user and **one** `ticker`, as follows:

```json
{
  "email": "test_user@gmail.com",
  "ticker": "TSLA"
}
```

- Service also has an end point for sending emails based on users subscribed tickers.
  It is used by parsing endpoint on hourly basis.

```shell
http://localhost:8002/notifications/email-fetched-news/
```

- The request and email for daily summary is set to 7 PM (Asia/Almaty time zone)
