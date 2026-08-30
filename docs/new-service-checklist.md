# New Service Checklist

When adding a new service, it is important to make sure a variety of auxiliary tasks are complete to keep the site secure, monitored, and running smoothly.
Some of these have been forgotten previously, which has caused issues. Therefore, it is better to be safe and have a defined procedure to follow.

1. Deploy service (Docker Compose)
   1. Does it follow the standard compose format?
   2. Does it have a unique port (if applicable)?
   3. Does it have a unique MAC and container name?
   4. Is it on the correct version label?
   5. Is it set to auto-update (or not)?
   6. Update relevant documentation.
2. Networking
   1. Assign an NPM entry.
   2. Assign a Pi-Hole local DNS entry.
   3. Make sure it is protected with authentication (if applicable).
3. Monitoring
   1. Add its entry to Uptime Kuma
   2. Add a health-check if lacking
   3. Add Grafana/Prometheus routes
   4. Add domain to pentest script (if applicable)
