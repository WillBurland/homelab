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

## Documentation

| Doc                                              | Covers                                           |
|--------------------------------------------------|--------------------------------------------------|
| [docs/authentication.md](docs/authentication.md) | OIDC/forward-auth status per service             |
| [docs/backup.md](docs/backup.md)                 | Backup strategies and procedures                 |
| [docs/hardware.md](docs/hardware.md)             | Physical server specs/details                    |
| [docs/mac-addresses.md](docs/mac-addresses.md)   | Pinned MAC addresses details                     |
| [docs/roadmap.md](docs/roadmap.md)               | Planned and completed work                       |
| [docs/secrets.md](docs/secrets.md)               | Required environmental variables per stack       |
| [docs/services.md](docs/services.md)             | Full service table, grouped by stack, with notes |
| [docs/setup.md](docs/setup.md)                   | Prerequisites, deployment steps                  |
