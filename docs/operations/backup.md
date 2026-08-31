# Backups

Backups are performed on a daily basis using [Zerobyte](https://github.com/nicotsx/zerobyte), a clean and modern web wrapper for Restic.

## Zerobyte

My Zerobyte instance has 1 job set up, which is to backup all of my Docker data/config, which are stored as host binds for ease of backing up and restoring.

This job runs daily at midnight and upon completion will mirror the repository to a Backblaze B2 bucket, satisfying the 3-2-1 backup rule:

1. Live/original copy (SSD/Apps pool).
2. 2nd media/device copy (HDD/NAS pool).
3. Offsite backup copy (Backblaze B2).

The job has a retention policy of 7 daily, 4 weekly and 6 monthly giving a good range of options for when a restoration is required.

## PC Backup

My PC runs its own local copy of Zerobyte with the same targets as the server (the HDD pool, and mirrored to Backblaze B2).
I initially tried to have these both be the same instance, with the server mounting my PC's shares when required, however, this turned out to be a lot more work than it was worth.

## Effectiveness

So far I have only had to restore a backup once, which was when I accidentally wiped `/home` on my PC.
The restoration worked completely flawlessly, restoring my files in minutes, proving its effectiveness.
A live restoration is yet to be required for my server, but that real world test has given me the confidence needed to trust the solution.
