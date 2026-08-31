# Setup

## Note

This isn't written as a general-purpose deployment guide, it's specific to my own hardware, domain, and network layout, and documented mainly so I have a record of how things fit together (and can rebuild if I need to).

If you're using this as a reference for your own homelab, expect to adapt most of it rather than follow it step-by-step.

## Prerequisites

This repo assumes you have a TrueNAS installation with 2 pools:

- NAS - The main HDD based, bulk storage pool.
- Apps - The SSD based, application pool.

You will also need a public domain which Cloudflare has access to/manages if you want a remote tunnel without a VPN/Tailscale.

## Deployment

1. In TrueNAS, deploy a Portainer instance from the built-in ix-apps.
2. In Portainer, deploy the stacks located in `/stacks`. These should be connected to a Git repo for easier updates.
3. Restore the config directories from backup.
4. Restart the stacks.
