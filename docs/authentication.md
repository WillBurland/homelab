# User Authentication

I am currently in the process of migrating from Cloudflare Zero Trust + Google OAuth to Authentik.

Services with native OIDC functionality will use Authentik directly, while others will use forward-auth via NPM.

## Applications

| Service             | Migrated | Auth Method  |
|---------------------|----------|--------------|
| Homepage            | No       | None         |
| Immich              | Yes      | OIDC         |
| Immich ML           | No       | N/A          |
| Immich Postgres     | No       | N/A          |
| Immich Redis        | No       | N/A          |
| Pacoloco            | No       | N/A          |
| Syncthing           | No       | Login        |
| WUD                 | No       | None         |
| Zerobyte            | No       | Login        |

## Authentication

| Service             | Migrated | Auth Method  |
|---------------------|----------|--------------|
| Authentik Server    | No       | Login        |
| Authentik Worker    | No       | N/A          |
| Authentik Postgres  | No       | N/A          |
| Vaultwarden         | No       | Login        |

## Development

| Service             | Migrated | Auth Method  |
|---------------------|----------|--------------|
| Forgejo             | Yes      | OIDC         |
| Forgejo DB          | No       | N/A          |

## Logging

| Service             | Migrated | Auth Method  |
|---------------------|----------|--------------|
| Grafana             | Yes      | OIDC         |
| Prometheus          | No       | None         |
| Scrutiny            | No       | Login        |
| Uptime Kuma         | No       | None         |

## Media

| Service             | Migrated | Auth Method  |
|---------------------|----------|--------------|
| Bazarr              | No       | None         |
| FileFlows           | No       | None         |
| Jackett             | No       | None         |
| Jellyfin            | No       | Login        |
| Komga               | Yes      | Forward auth |
| qBittorrent         | No       | None         |
| Radarr              | No       | None         |
| Seerr               | No       | Login        |
| Sonarr              | No       | None         |

## Networking

| Service             | Migrated | Auth Method  |
|---------------------|----------|--------------|
| Cloudflared         | No       | N/A          |
| FlareSolverr        | No       | N/A          |
| Nginx Proxy Manager | No       | Login        |
| Pi-Hole             | No       | Login        |
| Tailscale           | No       | N/A          |
