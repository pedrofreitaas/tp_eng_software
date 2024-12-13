-include .env

run:
	docker compose -f docker/docker-compose.yml --project-directory . up
