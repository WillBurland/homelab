#!/usr/bin/env bash
set -euo pipefail

APPS_DIR="./apps"
CONFIG_ROOT="$HOME/docker-data"

shopt -s nullglob
for compose_file in "$APPS_DIR"/*.yaml; do
	app_name=$(basename "$compose_file" .yaml)

	docker compose -f "$compose_file" down -v --remove-orphans

	config_dir="$CONFIG_ROOT/$app_name"
	if [[ -d "$config_dir" ]]; then
		rm -rf "$config_dir"
	fi
done

echo "[*] Removing all containers and volumes..."
docker ps -aq | xargs -r docker rm -f
docker volume ls -q | xargs -r docker volume rm

echo "[*] Done! All stacks, containers, and volumes removed. Images preserved."
