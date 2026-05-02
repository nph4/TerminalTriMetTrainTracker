import unittest
from datetime import datetime

from main import arrival
from stops import Line, STOPS, Direction


class TestArrival(unittest.TestCase):

    def test_non_interlined_stop(self):
        # Ruby Junction is Blue Line only
        stop_id = STOPS[Line.BLUE]["Ruby Junction/E 197th Ave"][Direction.EASTBOUND]
        result = arrival(stop_id, Line.BLUE)
        self.assertIsInstance(result, datetime)

    def test_interlined_stop(self):
        # Gateway TC is shared by Blue, Red, and Green
        stop_id = STOPS[Line.BLUE]["Gateway/NE 99th Ave TC"][Direction.WESTBOUND]
        result = arrival(stop_id, Line.BLUE)
        self.assertIsInstance(result, datetime)

    def test_invalid_stop_id(self):
        with self.assertRaises(ValueError):
            arrival(115022)

    def test_wrong_line_for_interlined_stop(self):
        # Washington Park is served by Blue and Red only, not Orange
        stop_id = STOPS[Line.BLUE]["Washington Park"][Direction.EASTBOUND]
        with self.assertRaises(ValueError):
            arrival(stop_id, Line.ORANGE)

    def test_no_line_specified(self):
        # Should return the next train regardless of line
        stop_id = STOPS[Line.BLUE]["Gateway/NE 99th Ave TC"][Direction.WESTBOUND]
        result = arrival(stop_id)
        self.assertIsInstance(result, datetime)

    def test_wrong_line_error_message_includes_valid_lines(self):
        # Washington Park is served by Blue and Red — both should appear in the error
        stop_id = STOPS[Line.BLUE]["Washington Park"][Direction.EASTBOUND]
        with self.assertRaises(ValueError) as ctx:
            arrival(stop_id, Line.ORANGE)
        message = str(ctx.exception)
        self.assertIn("Blue", message)
        self.assertIn("Red", message)


if __name__ == "__main__":
    unittest.main()
