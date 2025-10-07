#!/usr/bin/env bash
set -euo pipefail

APPS_DIR="./apps"
CONFIG_ROOT="$HOME/docker-data"

echo "[*] Pulling images..."
shopt -s nullglob
for compose_file in "$APPS_DIR"/*.yaml; do
	docker compose -f "$compose_file" pull
done
echo "[*] All images pulled successfully."

echo "[*] Deploying stacks..."
for compose_file in "$APPS_DIR"/*.yaml; do
	app_name=$(basename "$compose_file" .yaml)

	config_dir="$CONFIG_ROOT/$app_name/config"
	if [[ ! -d "$config_dir" ]]; then
		mkdir -p "$config_dir"
		chown -R 1000:1000 "$config_dir"
	fi

	docker compose -f "$compose_file" up -d --build
done

echo "[*] All apps deployed!"
