import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from stops import Line, STOPS

load_dotenv()

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


print(arrival(11502))