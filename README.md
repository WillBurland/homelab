# Docker Homelab Stack

## Overview

Self-hosted Docker homelab stack for media, monitoring, and personal services.
Designed to be reproducible via docker-compose and accessible through a reverse proxy.

Not included here is the TrueNAS and Portainer systems, as they are not deployed via docker-compose.

Remote access is granted either through Tailscale, or a Cloudflare tunnel, which requires a whitelisted Google OAuth login.

## Services

| Service             | Stack        | Access Control | Description               |
|---------------------|--------------|----------------|---------------------------|
| Bazarr              | Media        | Public         | Subtitle manager          |
| Cloudflared         | Networking   | N/A            | Remote tunnel             |
| FlareSolverr        | Networking   | N/A            | Index challenge solver    |
| Grafana             | Logging      | User/password  | Monitoring dashboard      |
| Homepage            | Applications | Public         | General homepage          |
| Jackett             | Media        | Public         | Torrent index/RSS manager |
| Jellyfin            | Media        | User/password  | Media client              |
| Jellyseerr          | Media        | User/password  | Media request manager     |
| Komga               | Media        | User/password  | Comic/manga client        |
| Nginx Proxy Manager | Networking   | User/password  | Reverse proxy             |
| Pi-Hole             | Networking   | User/password  | DNS adblocker             |
| Portainer           | N/A          | User/password  | Docker management         |
| Prometheus          | Logging      | Public         | Monitoring backend        |
| qBittorrent         | Media        | Public         | Torrent client            |
| Radarr              | Media        | Public         | Movie manager             |
| Sonarr              | Media        | Public         | TV-Show manager           |
| Syncthing           | Applications | User/password  | File synchronisation      |
| Tailscale           | Networking   | N/A            | Secure VPN                |
| TrueNAS WebUI       | N/A          | User/password  | NAS management            |
| Uptime Kuma         | Logging      | Public         | Service status page       |
| Vaultwarden         | Applications | User/password  | Password manager          |

**Public\*** -> When connected via LAN, Tailscale or Cloudflare tunnel

## Roadmap

- [X] Initial configuration/deployment
- [ ] Migrate Jellyseerr to Seerr project
- [ ] Zerobyte deployment
- [ ] InfluxDB deployment
- [ ] Node Exporter deployments
- [ ] SSO login (like Authentik)
- [ ] GitLab deployment
- [ ] Personal website host
- [ ] CI/CD website deployment

## Deployment

### Prerequisites

This repo assumes you have a TrueNAS installation with 2 pools:

- NAS - The main HDD based, bulk storage pool.
- Apps - The SSD based, application pool.

You will also need a public domain which Cloudflare has access to/manages if you want a remote tunnel without a VPN/Tailscale.

### Setup

1. In TrueNAS, deploy a Portainer instance from the built-in ix-apps.
2. In Portainer, deploy stacks for each of the entries in `/stacks`. Ideally these are fetched from a Git repo to make updates easier.
3. Deploy the stacks.
4. Restore the config directories from backup.
5. Restart the stacks.

## Mounts & directories

```text
mnt
|- Apps
|  |- Docker
|  \- Torrents
|     |- Complete
|     |- CompleteSources
|     \- Downloading
\- NAS
   |- Backups
   |  |- PC
   |  \- Docker
   |- Files
   \- Media
      |- Books
      |- Movies
      \- Shows
```

## Secrets

Most environment variables are committed in stack files.

The exceptions to this are required to be injected into the stack in Portainer:

- `CLOUDFLARE_TUNNEL_TOKEN`, in the networking stack.
- `TAILSCALE_AUTHKEY`, in the networking stack.
