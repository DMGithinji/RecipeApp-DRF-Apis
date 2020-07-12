[![Build Status](https://travis-ci.org/DMGithinji/RecipeApp.svg?branch=master)](https://travis-ci.org/DMGithinji/RecipeApp)

# RecipeAPI
An API backend (built using Django Rest Framework) for an app that enables users to save their favourite recipes



## Getting started

To start project, run:

```
docker-compose up
```

To run tests within the project, run:

```
docker-compose run app sh -c "python manage.py test && flake8"
```

The API will then be available at http://localhost:8000 and the documentation will be available using [Swagger](http://localhost:8000/swagger) or [Redoc](http://localhost:8000/redoc/)


### License and Copyright details

* [MIT LICENSE](LICENSE)
Copyright (c) 2020 **DMG**
