# `Shoppers Mart Inc.`

## This repository is responsible for `Shoppers Mart`'s ecommerce backend. It is build using Django-Oscar framework.
## The major implimentation is the integration of the backend with the Stripe to facilitate online payments.

# Instructions to setup the repo on the local machine:

## Python version
`python3 --version`

## Pip3 Install
`pip3 install pipenv`

## Pip3 Version
`pip3 --version`

## Creating env
`virtualenv .`

## Activating env
`source bin/activate`

## Seeing the currently installed packages in our env
`pip3 freeze`

## Installing all the dependencies
`pip3 install -r requirements.txt`

## Seeing the currently installed packages in our env
`pip3 freeze`

## Make migration
`python manage.py makemigrations`

## Run migration
`python manage.py migrate`

## Creating Superuser
`python manage.py createsuperuser`

## Run on local server
`python manage.py runserver`


## NOTE: Once the server is running, make sure to check the localhost port the server is running on. You will need to configure it for backend in the Shoppers Mart react frontend applciation.
