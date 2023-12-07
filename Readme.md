# Django Social APP

Welcome to the Social App, a dynamic web application enabling users to bookmark images through a bookmarklet and foster a sense of connection by following each other to discover the latest bookmarked images.

## Table of Contents

- [Prerequisites](#Prerequisites)
- [Getting Started](#getting-started)
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Usage](#usage)

## Prerequisites

Before you dive in, make sure you have the following requirements in place:

- [Python](https://www.python.org/)
- [Pipenv](https://pipenv.pypa.io/)
- [Redis](https://redis.io/)

Install the necessary Python packages within a virtual environment using the following command:

```
pipenv install
```

## Getting-started
- **Optional**: Initialize the app on Facebook, Twitter, and Google Developer platforms to enable OAuth2.

- Add the app configurations to the **'.env'** file in the project's root.<br> **Note :** that Social App APIs are optional for sign-in using OAuth2.

``` python
#Allowed Hosts
ALLOWED_HOSTS = ['bookmarkApp.com', 'localhost', '127.0.0.1']

# Facebook APP Data
SOCIAL_AUTH_FACEBOOK_KEY = 'XXXX' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'XXXX' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email'] # to ask facebook for the email of the user

# Twitter APP Data
SOCIAL_AUTH_TWITTER_KEY = 'XXXX' #Twitter API KEY
SOCIAL_AUTH_TWITTER_SECRET = 'XXXX' #Twitter API SECRET KEY

# Google APP Data
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'XXXX' #Google APP KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'XXXX' #Google APP SECRET KEY

# redis conf
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
```
- **Run the Redis server**. If Redis is not installed, [download and install it](https://redis.io/download). Then, start the Redis server.
``` bash
redis-server
```
- Apply migrations to the database:
``` bash
python3 manage.py makemigrations
```
``` bash
python3 manage.py migrate
```

## Introduction

The Social App is a comprehensive web application that leverages OAuth2 for user authentication. Users can seamlessly sign in using their Facebook, Twitter, or Google credentials. The app offers a range of features, allowing users to engage in an activity stream showcasing updates from people they follow, explore bookmarked images from all users, and seamlessly bookmark images using the bookmarklet.

## Technologies

- Python
- JavaScript
- HTML
- CSS
- Django
- Redis

## Usage
- Ensure that migrations are applied to the database:
``` bash
python3 manage.py makemigrations
```
``` bash
python3 manage.py migrate
```
- **Run the Redis server**. If not already running
``` bash
redis-server
```
- Start the App by running:
``` bash
python3 manage.py runserver_plus -cert-file cert.cert
```