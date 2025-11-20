# Docker Homelab Stack

## Getting started

1. Rename `.env.secrets.template` to `.env.secrets` and add in the relevant keys/logins
2. `./deploy.sh up -d` to start the stack
3. `docker compose down` to stop the stack

## Containers included

### Media

- Jellyfin
- Jellyseerr
- Komga
- Radarr
- Sonarr
- Bazarr
- qBittorrent
- Jackett

### Networking

- Cloudflared
- Flaresolverr
- Pi-Hole
- Nginx Proxy Manager

### System

- Homepage
- Uptime Kuma
- Prometheus
- Grafana
- Syncthing
- Vaultwarden
- Watchtower