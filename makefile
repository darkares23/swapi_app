# Variables
PROJECT_NAME=swapi_app
DJANGO_APP=api

# Comandos
build:
	@docker-compose build

up:
	@docker-compose up

down:
	@docker-compose down

migrations:
	@docker-compose run web python manage.py makemigrations $(DJANGO_APP)

migrate:
	@docker-compose run web python manage.py migrate

createsuperuser:
	@docker-compose run web python manage.py createsuperuser

shell:
	@docker-compose run web python manage.py shell

logs:
	@docker-compose logs -f

test:
	@docker-compose run web python manage.py test $(DJANGO_APP)

clean:
	@find . -name "*.pyc" -exec rm -f {} \;
