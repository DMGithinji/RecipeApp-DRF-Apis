[![Build Status](https://travis-ci.org/DMGithinji/RecipeApp.svg?branch=master)](https://travis-ci.org/DMGithinji/RecipeApp)


## RecipeAPI
An API backend (built using Django Rest Framework) for an app that enables users to save their favourite recipes

### Getting started

To start project, run:

```
docker-compose up
```

To run tests within the project, run:

```
docker-compose run app sh -c "python manage.py test && flake8"
```

The API will then be available at http://127.0.0.1:8000

The API documentation will be available at http://127.0.0.1:8000/swagger or http://127.0.0.1:8000/redoc/
