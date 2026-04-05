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

| Service             | Stack        | Exposure | Auth  | Description               |
|---------------------|--------------|----------|-------|---------------------------|
| Bazarr              | Media        | Internal | None  | Subtitle manager          |
| Cloudflared         | Networking   | Internal | N/A   | Remote tunnel             |
| FlareSolverr        | Networking   | Internal | N/A   | Index challenge solver    |
| Forgejo             | Development  | External | Login | Git server                |
| Forgejo DB          | Development  | Internal | N/A   | Forgejo Postgres Database |
| Grafana             | Logging      | Internal | Login | Monitoring dashboard      |
| Homepage            | Applications | Internal | None  | General homepage          |
| Jackett             | Media        | Internal | None  | Torrent index/RSS manager |
| Jellyfin            | Media        | Internal | Login | Media client              |
| Komga               | Media        | Internal | Login | Comic/manga client        |
| Nginx Proxy Manager | Networking   | Internal | Login | Reverse proxy             |
| Pi-Hole             | Networking   | Internal | Login | DNS adblocker             |
| Prometheus          | Logging      | Internal | None  | Monitoring backend        |
| qBittorrent         | Media        | Internal | None  | Torrent client            |
| Radarr              | Media        | Internal | None  | Movie manager             |
| Seerr               | Media        | Internal | Login | Media request manager     |
| Sonarr              | Media        | Internal | None  | TV-Show manager           |
| Syncthing           | Applications | Internal | Login | File synchronisation      |
| Tailscale           | Networking   | Internal | N/A   | Secure VPN                |
| Uptime Kuma         | Logging      | Internal | None  | Service status page       |
| Vaultwarden         | Applications | Internal | Login | Password manager          |
| WUD                 | Applications | Internal | None  | Docker container updater  |
| Zerobyte            | Applications | Internal | Login | Backup automation         |

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
- [ ] Expanded logging & monitoring
  - [ ] Deploy Node Exporters
  - [ ] Add container healthchecks
- [ ] SSO/OIDC login (e.g. Authentik)
- [ ] Deploy Home Assistant

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

Network stack:

- `CLOUDFLARE_TUNNEL_TOKEN`
- `TAILSCALE_AUTHKEY`

Applications stack:

- `WUD_HUB_USERNAME` - Docker Hub username
- `WUD_HUB_TOKEN` - Docker Hub access token
- `WUD_LSCR_USERNAME` - GitHub username
- `WUD_LSCR_TOKEN` - GitHub API token
- `ZEROBYTE_SECRET`
