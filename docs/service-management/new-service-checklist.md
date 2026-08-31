# New Service Checklist

When adding a new service, it is important to make sure a variety of auxiliary tasks are complete to keep the site secure, monitored, and running smoothly.
Some of these have been forgotten previously, which has caused issues. Therefore, it is better to be safe and have a defined procedure to follow.

Not all of these steps are applicable to every container, such as services without a UI or open port, so just ignore those steps.

## Deploy service (Docker Compose edits)

1. Does it follow the [standard compose format](compose-formatting.md)?
2. Does it have a unique:
   - Port.
   - Container name.
   - [MAC address](mac-addresses.md).
3. Is it on the correct version label?
4. Is it set to auto-update (or not)?
5. Add a health-check if lacking.
6. Update relevant documentation.

## Networking

1. Assign an NPM entry. Don't forget Authentik config!!!
2. Assign a Pi-Hole local DNS entry.

## Monitoring

1. Add its entry to Uptime Kuma.
2. Add Prometheus routes, deploying metric exporter if required.
3. Add Grafana dashboard.

## Miscellaneous

1. Add entry to Homepage.
2. Update pentest script domains, and run.
3. Double check access with reverse proxy.
