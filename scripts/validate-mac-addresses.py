#!/usr/bin/env python3

import sys
from pathlib import Path
from collections import defaultdict

import yaml

STACK_PREFIXES = {
    "applications": 0x06,
    "authentication": 0x0A,
    "development": 0x0E,
    "logging": 0x12,
    "media": 0x16,
    "networking": 0x1A,
    "system": 0x1E,
}


def format_mac(aa, bb, cc, dd):
    return f"{aa:02X}:{bb:02X}:{cc:02X}:{dd:02X}:00:00"


def check_compose(path):
    errors = []
    addresses = {}
    services = {}

    print(f"\nChecking: {path}")

    try:
        with path.open() as f:
            compose = yaml.safe_load(f)
    except Exception as e:
        print(f"  ERROR: Failed to parse YAML: {e}")
        return 1

    if not isinstance(compose, dict):
        return 0

    stack = path.parent.name.lower()
    expected_aa = STACK_PREFIXES.get(stack)

    if expected_aa is None:
        errors.append(f"Unknown stack directory: {stack}")

    for name, service in compose.get("services", {}).items():
        if not isinstance(service, dict):
            continue

        mac = service.get("mac_address")

        if not mac:
            errors.append(f"Missing MAC address: {name}")
            continue

        mac = str(mac).upper()

        if mac in addresses:
            errors.append(
                f"Duplicate MAC: {name}\n"
                f"    Actual:   {mac}\n"
                f"    Conflicts: {addresses[mac]}"
            )
        else:
            addresses[mac] = name

        parts = mac.split(":")

        if len(parts) != 6 or any(
            len(p) != 2 or not all(
                c in "0123456789ABCDEF" for c in p
            )
            for p in parts
        ):
            errors.append(
                f"Invalid MAC format: {name}\n"
                f"    Actual:   {mac}\n"
                f"    Expected: AA:BB:CC:DD:00:00"
            )
            continue

        aa, bb, cc, dd, ee, ff = (
            int(p, 16) for p in parts
        )

        if expected_aa is not None and aa != expected_aa:
            errors.append(
                f"Incorrect stack prefix: {name}\n"
                f"    Actual:   {mac}\n"
                f"    Expected: {format_mac(expected_aa, bb, cc, dd)}"
            )

        if aa % 4 != 2:
            errors.append(
                f"Invalid first octet: {name}\n"
                f"    Actual:   {mac}\n"
                f"    Expected: First octet must be 2 mod 4"
            )

        if ee != 0 or ff != 0:
            errors.append(
                f"Invalid trailing octets: {name}\n"
                f"    Actual:   {mac}\n"
                f"    Expected: {format_mac(aa, bb, cc, dd)}"
            )

        services[name] = (aa, bb, cc, dd, mac)

    # Check service IDs.
    service_ids = sorted({v[1] for v in services.values()})
    expected_ids = list(range(1, len(service_ids) + 1))

    if service_ids != expected_ids:
        for actual, expected in zip(
            service_ids, expected_ids
        ):
            if actual != expected:
                for name, (aa, bb, cc, dd, mac) in services.items():
                    if bb == actual:
                        errors.append(
                            f"Incorrect service ID: {name}\n"
                            f"    Actual:   {mac}\n"
                            f"    Expected: "
                            f"{format_mac(aa, expected, cc, dd)}"
                        )
                break

    # Group components by service ID.
    components = defaultdict(set)
    exporters = defaultdict(set)

    for name, (aa, bb, cc, dd, mac) in services.items():
        components[bb].add(cc)
        exporters[(bb, cc)].add(dd)

    # Check component IDs.
    for bb, values in components.items():
        found = sorted(values)
        expected = list(range(1, len(found) + 1))

        if found != expected:
            for name, (aa, service, cc, dd, mac) in services.items():
                if service != bb:
                    continue

                expected_cc = expected[found.index(cc)] if cc in found else cc

                if cc != expected_cc:
                    errors.append(
                        f"Incorrect component ID: {name}\n"
                        f"    Actual:   {mac}\n"
                        f"    Expected: "
                        f"{format_mac(aa, bb, expected_cc, dd)}"
                    )

    # Check exporter IDs.
    for (bb, cc), values in exporters.items():
        found = sorted(values)
        expected = list(range(len(found)))

        if found != expected:
            for name, (aa, service, component, dd, mac) in services.items():
                if service != bb or component != cc:
                    continue

                expected_dd = expected[found.index(dd)]

                if dd != expected_dd:
                    errors.append(
                        f"Incorrect exporter ID: {name}\n"
                        f"    Actual:   {mac}\n"
                        f"    Expected: "
                        f"{format_mac(aa, bb, cc, expected_dd)}"
                    )

    if errors:
        for error in errors:
            print(f"  ERROR: {error.replace(chr(10), chr(10) + '  ')}")
    else:
        print(f"  OK: {len(services)} MAC addresses validated.")

    return len(errors)


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")

    files = sorted(
        p for p in root.rglob("*")
        if p.is_file() and p.name == "docker-compose.yml"
    )

    if not files:
        print("No Compose files found.")
        sys.exit(1)

    total_errors = 0

    for path in files:
        total_errors += check_compose(path)

    print(
        f"\nFinished: {len(files)} files checked, "
        f"{total_errors} errors found."
    )

    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
