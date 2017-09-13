## Join us on Slack!

https://theseus-slack.now.sh/

## Feature Requests

We're currently accepting feature requests to help shape the future of the project. [Check us out on Canny!](https://theseus.canny.io/feature-requests)

## About Theseus

Theseus is a modern and FOSS alternative to ConnectWise. [Check out the Reddit post that start it all](https://www.reddit.com/r/msp/comments/6wozns/open_source_competitor_to_connectwise/). We're currently focusing on ticketing and CRM. For technical details you can read the wiki on this repository and [join the conversation in Slack](https://theseus-slack.now.sh/).

## Developers

**Setting up the development environment**

`docker-compose up`

Sometimes the docker-compose service for web doesn't sync up with the database. It's a known issue. Simply run `docker-compose down` and then `docker-compose up` until it goes down, then you can add `-d` for daemon mode.

`docker-compose run web code/manage.py createsuperuser`

This is your administrative user.

`docker-compose run web code/manage.py makemigrations`

This gets your migrations files caught up.

`docker-compose run web code/manage.py migrate`

This builds the tables.

`docker-compose run web code/manage.py loaddata organizations`

This loads the test data into the database.

Your development environment is now ready for dev!

**Adding an app**

1. Use the Django CLI to start the app inside the `theseus` directory.

2. Add your app to `settings.py` on **below** line 42
