# Static MAC Addressing

Docker normally auto-generates a container's MAC address by hashing/encoding its IP address on the bridge.
This works fine for stable containers, but breaks horribly with recreated containers, with something like Watchtower updating containers.

Docker has a known bug where a recreated container can retain a stale, cached MAC address instead of recalculating one against its current IP.
As IPs get recycled across restarts, two unrelated containers can end up sharing a MAC and things get bad from there, with very strange network issues such as two different containers responding to the same ping.

To fix this in this setup, we need to assign every container a permanent, explicit MAC address in the compose files. This removed the Docker auto-assignment issues entirely, and as a bonus let us assign a more organised formatting standard to the addresses.

## The Scheme

Format: `AA:BB:CC:00:00:00`

| Octet | Meaning   | Notes                                                              |
|-------|-----------|--------------------------------------------------------------------|
| `AA`  | Stack     | Fixed per compose stack                                            |
| `BB`  | Service   | Sequential per service within the stack, starting at `01`          |
| `CC`  | Component | `01` for a service's primary container, `02`, `03`... for sidecars |

## Stack Prefixes (`AA`)

| Prefix | Stack                 |
|--------|-----------------------|
| `02`   | Unused/Docker default |
| `06`   | Applications          |
| `0A`   | Authentication        |
| `0E`   | Development           |
| `12`   | Logging               |
| `16`   | Media                 |
| `1A`   | Networking            |

The MAC address first octet has specific restrictions for the first octet, forcing them to be `2 mod 4`, hence the spacing.

## Examples

### Single-container Service

| Container | MAC Address         |
|-----------|---------------------|
| `bazarr`  | `16:01:01:00:00:00` |

### Multi-container Service

| Container         | MAC Address         |
|-------------------|---------------------|
| `immich`          | `06:02:01:00:00:00` |
| `immich-ml`       | `06:02:02:00:00:00` |
| `immich-postgres` | `06:02:03:00:00:00` |
| `immich-redis`    | `06:02:04:00:00:00` |
