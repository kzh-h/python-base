docker_compose_build_builder:
	docker compose -f compose.build.yaml build

docker_compose_development_up:
	docker compose -f compose.development.yaml up -d

docker_compose_development_build_and_up:
	docker compose -f compose.development.yaml up -d --build