# Docker Homelab Stack

## Important Repo Info

The [GitHub](https://github.com/WillBurland/homelab) repository is the **primary source** for the Homelab Docker stack. The Forgejo repository is a mirror which is updated every 24 hours.

This arrangement avoids chicken-and-egg issues when deploying Docker Compose from inside a container, ensuring that deployments always fetch a stable copy of the stack without waiting for mirror updates or requiring manual synchronisation.

## Overview

Self-hosted Docker homelab stack for media, monitoring, and personal services.
Designed to be reproducible via docker-compose and accessible through a reverse proxy.

TrueNAS and Portainer are not included here, as they are not deployed via docker-compose.

Remote access is granted either through Tailscale, or a Cloudflare tunnel, which requires a whitelisted Google OAuth login.

## Architecture

```text
TrueNAS
├─ ix-apps
│  └─ Portainer
│
├─ Docker Stacks
│  ├─ Applications
│  ├─ Authentication
│  ├─ Development
│  ├─ Logging
│  ├─ Media
│  └─ Networking
│
└─ ZFS Pools
   ├─ Apps
   │  ├─ Docker Data
   │  └─ Torrents
   │
   └─ NAS
      ├─ Backups
      ├─ Files
      └─ Media
         ├─ Books
         ├─ Movies
         └─ Shows
```

## Services

| Service             | Stack          | Auth Method  | Description                 |
|---------------------|----------------|--------------|-----------------------------|
| Authentik Server    | Authentication | Login        | SSO/OIDC identity provider  |
| Authentik Worker    | Authentication | N/A          | Background task processor   |
| Authentik Postgres  | Authentication | N/A          | Authentik Postgres database |
| Bazarr              | Media          | None         | Subtitle manager            |
| Cloudflared         | Networking     | N/A          | Remote tunnel               |
| FileFlows           | Media          | None         | Automated media pipelines   |
| FlareSolverr        | Networking     | N/A          | Index challenge solver      |
| Forgejo             | Development    | OIDC         | Git server                  |
| Forgejo DB          | Development    | N/A          | Forgejo Postgres database   |
| Grafana             | Logging        | OIDC         | Monitoring dashboard        |
| Homepage            | Applications   | None         | General homepage            |
| Immich              | Applications   | OIDC         | Photo storage/server        |
| Immich ML           | Applications   | N/A          | Immich ML inference         |
| Immich Postgres     | Applications   | N/A          | Immich Postgres database    |
| Immich Redis        | Applications   | N/A          | Immich job queue/cache      |
| Jackett             | Media          | None         | Torrent index/RSS manager   |
| Jellyfin            | Media          | Login        | Media client                |
| Komga               | Media          | Forward auth | Comic/manga client          |
| Nginx Proxy Manager | Networking     | Login        | Reverse proxy               |
| Pacoloco            | Applications   | N/A          | Pacman cache/prefetcher     |
| Pi-Hole             | Networking     | Login        | DNS adblocker               |
| Prometheus          | Logging        | None         | Monitoring backend          |
| qBittorrent         | Media          | None         | Torrent client              |
| Radarr              | Media          | None         | Movie manager               |
| Scrutiny            | Logging        | Login        | Drive monitoring            |
| Seerr               | Media          | Login        | Media request manager       |
| Sonarr              | Media          | None         | TV-Show manager             |
| Syncthing           | Applications   | Login        | File synchronisation        |
| Tailscale           | Networking     | N/A          | Secure VPN                  |
| Uptime Kuma         | Logging        | None         | Service status page         |
| Vaultwarden         | Authentication | Login        | Password manager            |
| WUD                 | Applications   | None         | Docker container updater    |
| Zerobyte            | Applications   | Login        | Backup automation           |

## Roadmap

- [X] Initial configuration & deployment
- [X] Migrate Jellyseerr to Seerr project
- [X] What's Up Docker (WUD)
  - [X] Deploy
  - [X] Configure automatic updates for selected containers
- [X] Zerobyte
  - [X] Deploy
  - [X] Migrate local PC instance
- [X] Deploy Forgejo
- [X] Deploy personal website
- [X] SSO/OIDC login (e.g. Authentik)
  - [ ] Migrate relevant services to use it
  - [ ] Expose relevant services to the internet
- [ ] Expanded logging & monitoring
  - [ ] Deploy Node Exporters
  - [ ] Add container healthchecks
- [ ] Deploy Home Assistant
- [ ] Separate/restrict Docker networks

## Deployment

### Prerequisites

This repo assumes you have a TrueNAS installation with 2 pools:

- NAS - The main HDD based, bulk storage pool.
- Apps - The SSD based, application pool.

You will also need a public domain which Cloudflare has access to/manages if you want a remote tunnel without a VPN/Tailscale.

### Setup

1. In TrueNAS, deploy a Portainer instance from the built-in ix-apps.
2. In Portainer, deploy the stacks located in `/stacks`. These should be connected to a Git repo for easier updates.
3. Restore the config directories from backup.
4. Restart the stacks.

## Secrets

Most environment variables are committed in stack files.

The following secrets must be injected via Portainer at deployment time:

Applications stack:

- `WUD_HUB_USERNAME` - Docker Hub username
- `WUD_HUB_TOKEN` - Docker Hub access token
- `WUD_LSCR_USERNAME` - GitHub username
- `WUD_LSCR_TOKEN` - GitHub API token
- `ZEROBYTE_SECRET`

Authentication stack:

- `AUTHENTIK_SECRET_KEY`

Logging stack:

- `GRAFANA_AUTH_SECRET` - Grafana Authentik secret

Networking stack:

- `CLOUDFLARE_TUNNEL_TOKEN`
- `TAILSCALE_AUTHKEY`
