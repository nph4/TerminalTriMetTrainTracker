import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from stops import Line, STOPS

load_dotenv()

_LINE_COLOR = {
    Line.BLUE:   "\033[94m",        # bright blue
    Line.RED:    "\033[91m",        # bright red
    Line.YELLOW: "\033[93m",        # bright yellow
    Line.GREEN:  "\033[92m",        # bright green
    Line.ORANGE: "\033[38;5;208m",  # 256-color orange (no standard ANSI slot)
}
_RESET = "\033[0m"


def _color_line(line: Line) -> str:
    return f"{_LINE_COLOR[line]}{line.value}{_RESET}"


_ROUTE_ID = {
    Line.BLUE:   100,
    Line.RED:    90,
    Line.YELLOW: 190,
    Line.GREEN:  200,
    Line.ORANGE: 290,
}

_ARRIVALS_URL = "https://developer.trimet.org/ws/V2/arrivals"

_VALID_STOP_IDS = {
    id for line in STOPS.values() for dirs in line.values() for id in dirs.values()
}

_STOP_LINES: dict[int, set[Line]] = {}
for _line, _stations in STOPS.items():
    for _dirs in _stations.values():
        for _id in _dirs.values():
            _STOP_LINES.setdefault(_id, set()).add(_line)


def arrival(stop_id: int, line: Line | None = None) -> datetime | None:
    if stop_id not in _VALID_STOP_IDS:
        raise ValueError(f"Invalid stop ID: {stop_id}")
    if line is not None and line not in _STOP_LINES[stop_id]:
        valid = ", ".join(l.value for l in sorted(_STOP_LINES[stop_id], key=lambda l: l.value))
        raise ValueError(f"{line.value} Line does not serve stop {stop_id} (served by: {valid})")
    response = requests.get(
        _ARRIVALS_URL,
        params={"locIDs": stop_id, "appID": os.environ["APIKEY"]},
    )
    response.raise_for_status()

    arrivals = response.json()["resultSet"].get("arrival", [])
    target_route = _ROUTE_ID[line] if line else None
    now_ms = datetime.now().timestamp() * 1000
    earliest_ms: int | None = None

    for arr in arrivals:
        if arr.get("routeSubType") != "Light Rail":
            continue
        if target_route is not None and arr["route"] != target_route:
            continue
        arrival_ms = arr.get("estimated") or arr.get("scheduled")
        if arrival_ms and arrival_ms > now_ms:
            if earliest_ms is None or arrival_ms < earliest_ms:
                earliest_ms = arrival_ms

    return datetime.fromtimestamp(earliest_ms / 1000) if earliest_ms is not None else None


def _menu(prompt: str, options: list[str]) -> int:
    print()
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    print()
    while True:
        raw = input(f"{prompt} (1-{len(options)}, q to quit): ").strip()
        if raw.lower() == "q":
            raise SystemExit(0)
        try:
            choice = int(raw)
            if 1 <= choice <= len(options):
                return choice - 1
        except ValueError:
            pass
        print(f"  Enter a number between 1 and {len(options)}.")


def _select_stop() -> tuple[int, Line]:
    lines = list(STOPS.keys())
    line = lines[_menu("Select a line", [_color_line(l) for l in lines])]

    stations = list(STOPS[line].keys())
    station = stations[_menu(f"Select a {_color_line(line)} Line station", stations)]

    dirs = STOPS[line][station]
    if len(dirs) == 1:
        direction = next(iter(dirs))
        print(f"\n  Direction: {direction.value} (only option at this terminus)")
    else:
        direction_list = list(dirs.keys())
        direction = direction_list[_menu("Select a direction", [d.value for d in direction_list])]

    return dirs[direction], line


def main() -> None:
    print("TriMet MAX Train Arrival Tracker")
    print("================================")
    stop_id, line = _select_stop()
    print(f"\nFetching next {_color_line(line)} Line arrival for stop {stop_id}...")
    result = arrival(stop_id, line)
    if result is None:
        print("No upcoming arrivals found.")
    else:
        minutes = int((result - datetime.now()).total_seconds() / 60)
        print(f"Next arrival: {result.strftime('%I:%M %p')} ({minutes} min)")


if __name__ == "__main__":
    main()