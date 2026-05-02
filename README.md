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
```
python -m unittest tests -v
```
Note: `test_non_interlined_stop` and `test_interlined_stop` make live API calls and assert that a datetime is returned. These will fail outside of MAX operating hours when no arrivals are scheduled.


## Should I actually use this?
**NO**
TriMet has much better tools on their website. This is a personal project that mostly exists for me to learn how to work with GTFS systems.