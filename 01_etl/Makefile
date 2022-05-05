lint:
	isort ./app && flake8 ./app
up:
	docker-compose -f docker-compose.yml up -d
down:
	docker-compose -f docker-compose.yml down
build:
	docker-compose -f docker-compose.yml up -d --build
rebuild:
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.yml up -d --build
translation:
	django-admin makemessages -l ru
translate:
	django-admin compilemessages -l ru