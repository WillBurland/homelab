# Hardware

## Server Chassis

| Part      | Specification         | Notes                         |
|-----------|-----------------------|-------------------------------|
| CPU       | AMD Ryzen 5 4500      | 6C12T - 65W                   |
| RAM       | 48GB DDR4 3200 MT/s   | 2 x 8GB & 2 x 16GB            |
| GPU       | Intel ARC A380        | Used for Jellyfin transcoding |
| Case      | Codegen 4U CSCG4U600E | 15 x 3.5" drive bays          |

## HDD Pool

3 x 6TB Seagate SATA HDDs running in RAIDZ1.

I have 6 x 6TB refurbished SAS drives and a LSI 9300-16I SAS HBA, but haven't got around to installing these yet.
I probably would have to upgrade the case fans to support these as they seemed to run quite hot in my testing, but this isn't a priority as I'm not short on space yet.
When set up, I would likely run these in RAIDZ2, and retire my SATA drives to be used as cold storage or emergency swaps in case of a SAS drive failure.

## SSD Pool

1 x 512GB NVMe + 1 x 2TB NVMe, running in stripe.

Redundancy is not a concern here at all, as the SSD pool is just where my apps operate.
Capacity and speed is the larger concern, as qBittorrent uses most of this space for seeding.

All my Docker apps store their data on this pool, however, this is still not a real concern as the whole Docker data directory is backed up. This is detailed in [backup.md](backup.md).
