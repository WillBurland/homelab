# Hardware

## Server Chassis

| Part | Specification         | Notes                         |
|------|-----------------------|-------------------------------|
| CPU  | AMD Ryzen 5 4500      | 6C12T - 65W                   |
| RAM  | 48GB DDR4 3200 MT/s   | 2 x 8GB & 2 x 16GB            |
| GPU  | Intel ARC A380        | Used for Jellyfin transcoding |
| Case | Codegen 4U CSCG4U600E | 15 x 3.5" drive bays          |

## HDD Pool

6 x 6TB refurbished SAS HDDs running in RAIDZ2. In order to interface with the drives I have a LSI 9300-16i SAS HBA.

I have 3 x 6TB Seagate SATA HDDs acting as cold spares or potential cold storage/backup, which used to be used as my main HDD Pool.

## SSD Pool

1 x 2TB NVMe.

Redundancy is not a concern here at all, as the SSD pool is just where my apps operate.
Capacity and speed is the larger concern, as qBittorrent uses most of this space for seeding.

All my Docker apps store their data on this pool, however, this is still not a real concern as the whole Docker data directory is backed up. This is detailed in [docs/operations/backup.md](../operations/backup.md).
