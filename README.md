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
│  ├─ Networking
│  └─ System
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

Docs live under [`docs/`](docs/), grouped by category:

| Category                                        | Covers                                                    |
|-------------------------------------------------|-----------------------------------------------------------|
| [getting-started/](docs/getting-started/)       | Prerequisites and deployment steps                        |
| [service-management/](docs/service-management/) | Conventions and procedure for adding/maintaining services |
| [reference/](docs/reference/)                   | Current-state lookups, services, auth, secrets, hardware  |
| [operations/](docs/operations/)                 | Ongoing maintenance procedures (backups, etc.)            |
| [misc/](docs/misc/)                             | Planning and anything that doesn't fit elsewhere          |
