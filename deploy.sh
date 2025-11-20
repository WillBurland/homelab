#!/usr/bin/env bash
set -e

set -a
source .env
source .env.secrets
set +a

process_file() {
    local INPUT="$1"
    local OUT_DIR="$2"
    local MODE="$3"

    OUT_DIR=$(eval echo "$OUT_DIR")

    mkdir -p "$OUT_DIR"

    local BASENAME
    BASENAME="$(basename "$INPUT")"

    local OUTPUT="${OUT_DIR}/${BASENAME}"

    case "$MODE" in
        sub)
            envsubst < "$INPUT" > "$OUTPUT"
            echo "Subbed: $INPUT → $OUTPUT"
            ;;
        copy)
            cp "$INPUT" "$OUTPUT"
            echo "Copied: $INPUT → $OUTPUT"
            ;;
    esac
}

echo "$CONFIGS" | while IFS='|' read -r INPUT OUT_DIR MODE; do
    [[ -z "$INPUT$OUT_DIR$MODE" ]] && continue

    INPUT=$(echo "$INPUT" | xargs)
    OUT_DIR=$(echo "$OUT_DIR" | xargs)
    MODE=$(echo "$MODE" | xargs)

    process_file "$INPUT" "$OUT_DIR" "$MODE"
done

exec docker compose "$@"