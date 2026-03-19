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

| Service             | Stack        | Access Control | Description               |
|---------------------|--------------|----------------|---------------------------|
| Bazarr              | Media        | Public         | Subtitle manager          |
| Cloudflared         | Networking   | N/A            | Remote tunnel             |
| FlareSolverr        | Networking   | N/A            | Index challenge solver    |
| Forgejo             | Applications | User/password  | Git server                |
| Forgejo DB          | Applications | N/A            | Forgejo Postgres Database |
| Grafana             | Logging      | User/password  | Monitoring dashboard      |
| Homepage            | Applications | Public         | General homepage          |
| Jackett             | Media        | Public         | Torrent index/RSS manager |
| Jellyfin            | Media        | User/password  | Media client              |
| Komga               | Media        | User/password  | Comic/manga client        |
| Nginx Proxy Manager | Networking   | User/password  | Reverse proxy             |
| Pi-Hole             | Networking   | User/password  | DNS adblocker             |
| Prometheus          | Logging      | Public         | Monitoring backend        |
| qBittorrent         | Media        | Public         | Torrent client            |
| Radarr              | Media        | Public         | Movie manager             |
| Seerr               | Media        | User/password  | Media request manager     |
| Sonarr              | Media        | Public         | TV-Show manager           |
| Syncthing           | Applications | User/password  | File synchronisation      |
| Tailscale           | Networking   | N/A            | Secure VPN                |
| Uptime Kuma         | Logging      | Public         | Service status page       |
| Vaultwarden         | Applications | User/password  | Password manager          |
| WUD                 | Applications | Public         | Docker container updater  |
| Zerobyte            | Applications | User/password  | Backup automation         |

**Public\*** = Accessible via LAN, Tailscale or Cloudflare tunnel

## Roadmap

- [X] Initial configuration & deployment
- [X] Migrate Jellyseerr to Seerr project
- [X] What's Up Docker (WUD)
  - [X] Deploy
  - [X] Configure automatic updates for selected containers
- [X] Zerobyte
  - [X] Deploy
  - [X] Migrate local PC instance
- [ ] Expanded logging & monitoring
  - [ ] Deploy InfluxDB
  - [ ] Deploy Node Exporters
  - [ ] Add container healthchecks
- [ ] SSO/OIDC login (e.g. Authentik)
- [ ] Personal website hosting
- [ ] Git ecosystem
  - [X] Deploy Forgejo
  - [ ] Deploy Docker container registry
  - [ ] CI/CD for website deployment

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

- `WUD_LSCR_USERNAME` - GitHub username
- `WUD_LSCR_TOKEN` - GitHub API token
- `ZEROBYTE_SECRET`
