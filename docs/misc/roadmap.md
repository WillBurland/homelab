# Roadmap

## Todo Next

- [ ] **DEPLOY** - Exporters for services.
- [ ] **CONFIG** - Prometheus scraping for all exporters.
- [ ] **CONFIG** - Grafana dashboards for all Prometheus targets.

## Future Ideas

- [ ] **MIGRATE** - Raw Docker Socket mounts to Docker Socket Proxy container where possible.
- [ ] **CONFIG** - Remove any unnecessary port exposure, use Docker DNS when possible.
- [ ] **RESEARCH** - Non-native OIDC integration for services using forward-auth.
- [ ] **CONFIG** - Separate/restrict Docker networks.
- [ ] **DEPLOY** - Container new release RSS notifications.
- [ ] **DEPLOY** - Home Assistant.

## Done

- [x] **DEPLOY** - Initial configuration & deployment.
- [x] **MIGRATE** - Jellyseerr to Seerr.
- [x] **DEPLOY** - Watchtower (modern fork).
- [x] **CONFIG** - Assign containers auto-update strategies.
- [x] **DEPLOY** - Zerobyte.
- [x] **DEPLOY** - Forgejo.
- [x] **DEPLOY** - Personal website.
- [x] **DEPLOY** - Authentik.
- [x] **MIGRATE** - Cloudflare Zero Trust/OAuth to Authentik OIDC.
- [x] **CONFIG** - Container healthchecks where not provided in base image.
