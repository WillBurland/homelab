# Docker Homelab Stack

## Getting started

1. Deploy the stack with `./stack up all`
2. Do the basic GUI setup in each container
3. Rename `.env.secrets.template` to `.env.secrets` and add in the relevant keys/logins
4. `./stack restart all` to apply the changes

## Stack ecosystem

### Applications

- Homepage
- Syncthing
- Vaultwarden

### Logging

- Grafana
- Prometheus
- Uptime Kuma

### Media

- Bazarr
- Jackett
- Jellyfin
- Jellyseerr
- Komga
- qBittorrent
- Radarr
- Sonarr

### Networking

- Cloudflared
- Flaresolverr
- Nginx Proxy Manager
- Pi-Hole
- Tailscale

### System

- Portainer (not included)
- TrueNAS (not included)
- Watchtower