# Secrets

Non-secret environment variables are committed in stack files.

The following secrets must be injected via Portainer at deployment time.
If an entry doesn't have a description, then its a standard secret/key, refer to online docs.

## Applications

| Variable          | Description |
|-------------------|-------------|
| `ZEROBYTE_SECRET` | -           |

## Authentication

| Variable               | Description |
|------------------------|-------------|
| `AUTHENTIK_SECRET_KEY` | -           |

## Development

None.

## Logging

| Variable              | Description               |
|-----------------------|---------------------------|
| `GRAFANA_AUTH_SECRET` |  Grafana Authentik secret |

## Media

None.

## Networking

| Variable                  | Description |
|---------------------------|-------------|
| `CLOUDFLARE_TUNNEL_TOKEN` | -           |
| `TAILSCALE_AUTHKEY`       | -           |

## System

| Variable                     | Description     |
|------------------------------|-----------------|
| `WATCHTOWER_DISCORD_WEBHOOK` | Token@WebhookID |
