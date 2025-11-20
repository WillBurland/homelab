#!/usr/bin/env bash
set -a
source .env
source .env.secrets
set +a

exec docker compose "$@"