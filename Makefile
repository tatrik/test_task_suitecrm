build:
	docker-compose -f docker-compose.yaml build

migrations:
	docker-compose -f docker-compose.yaml run web alembic upgrade head

up:
	docker compose -f docker-compose.yaml up

down:
	docker compose -f docker-compose.yaml down && docker network prune --force
