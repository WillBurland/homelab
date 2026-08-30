# Secrets

Most environment variables are committed in stack files.

The following secrets must be injected via Portainer at deployment time:

## Applications stack

- `ZEROBYTE_SECRET`

## Authentication stack

- `AUTHENTIK_SECRET_KEY`

## Logging stack

- `GRAFANA_AUTH_SECRET` - Grafana Authentik secret

## Networking stack

- `CLOUDFLARE_TUNNEL_TOKEN`
- `TAILSCALE_AUTHKEY`

## System stack

- `WATCHTOWER_DISCORD_WEBHOOK` - Token@WebhookID
