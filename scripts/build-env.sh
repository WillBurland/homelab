#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GLOBAL_ENV="$ROOT_DIR/.env.global"

for stack in "$ROOT_DIR"/stacks/*; do
    [ -d "$stack" ] || continue

    STACK_ENV="$stack/.env.stack"
    TARGET_ENV="$stack/.env"

    if [ -f "$STACK_ENV" ]; then
        {
            echo "# --------------------------------------"
            echo "#          AUTO-GENERATED FILE"         
            echo "# Source: .env.global + .env.stack"
            echo "# Run scripts/build-env.sh to regenerate"
            echo "# --------------------------------------"
            echo
            cat "$GLOBAL_ENV"
            echo
            cat "$STACK_ENV"
        } > "$TARGET_ENV"

        echo "Generated $TARGET_ENV"
    fi
done
