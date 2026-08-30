# User Authentication

Services with native OIDC functionality use Authentik directly, while others will use forward-auth via NPM.

Some services are not to be behind ID verification at all, namely Vaultwarden and Authentik itself. This is to ensure access is always granted for browser extension access for example.
In these cases, strong credentials and 2FA are used for obvious reasons.

## Applications

| Service         | Auth Method  |
|-----------------|--------------|
| Homepage        | Forward auth |
| Immich Server   | OIDC         |
| Immich ML       | -            |
| Immich Postgres | -            |
| Immich Redis    | -            |
| Syncthing       | Forward auth |
| Zerobyte        | Forward auth |

## Authentication

| Service            | Auth Method  |
|--------------------|--------------|
| Authentik Server   | Login        |
| Authentik Worker   | -            |
| Authentik Postgres | -            |
| Vaultwarden        | Login        |

## Development

| Service    | Auth Method  |
|------------|--------------|
| Forgejo    | OIDC         |
| Forgejo DB | -            |

## Logging

| Service     | Auth Method  |
|-------------|--------------|
| Grafana     | OIDC         |
| Prometheus  | Forward auth |
| Scrutiny    | Forward auth |
| Uptime Kuma | Forward auth |

## Media

| Service     | Auth Method  |
|-------------|--------------|
| Bazarr      | Forward auth |
| FileFlows   | Forward auth |
| Jackett     | Forward auth |
| Jellyfin    | Forward auth |
| Komga       | Forward auth |
| qBittorrent | Forward auth |
| Radarr      | Forward auth |
| Seerr       | Forward auth |
| Sonarr      | Forward auth |

## Networking

| Service             | Auth Method  |
|---------------------|--------------|
| Cloudflared         | -            |
| FlareSolverr        | -            |
| Nginx Proxy Manager | Forward auth |
| Pi-Hole             | Forward auth |
| Tailscale           | -            |

## System

| Service      | Auth Method  |
|--------------|--------------|
| Docker Proxy | -            |
| Pacoloco     | -            |
| Watchtower   | -            |
