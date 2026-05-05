# TerminalTriMetTrainTracker

A project to create a terminal based transit tracker app for TriMet's MAX Light Rail

## Dependencies

- gtfs-realtime-bindings
- requests
- protobuf
- python-dotenv
- [TriMet API Key](https://developer.trimet.org/)

### Notes on TriMet's API Rate Limits

- Trimet requests that you poll no more than once every 30 seconds for realtime feeds.

## Running Tests

``` bash
python -m unittest tests -v
```

Note: `test_non_interlined_stop` and `test_interlined_stop` make live API calls and assert that a datetime is returned. These will fail outside of MAX operating hours when no arrivals are scheduled.

## Usage

``` bash
python3 main.py
```

- Choose the line that you want
- Choose the station
- Choose the direction that you are travelling
- Note, for terminus stops it will automatically choose your direction of travel, because you can only travel in one direction

## Should I actually use this for trip planning?

**NO**
TriMet has much better tools on their website. This is a personal project that mostly exists for me to learn how to work with GTFS systems

## AI Usage statement

AI was used in making this repo. I'm still learning, so bounced some ideas on how to structure the stops.py information. I had it help me write my tests, and had it set the line color to match the line name.
