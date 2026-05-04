import unittest
from datetime import datetime
from unittest.mock import patch

from main import arrival, _menu, _select_stop
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


class TestMenu(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', return_value='2')
    def test_valid_input_returns_zero_based_index(self, _input, _print):
        self.assertEqual(_menu("Choose", ["A", "B", "C"]), 1)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['0', 'abc', '4', '2'])
    def test_invalid_input_reprompts_until_valid(self, mock_input, _print):
        result = _menu("Choose", ["A", "B", "C"])
        self.assertEqual(result, 1)
        self.assertEqual(mock_input.call_count, 4)

    @patch('builtins.print')
    @patch('builtins.input', return_value='q')
    def test_q_exits(self, _input, _print):
        with self.assertRaises(SystemExit):
            _menu("Choose", ["A", "B", "C"])

    @patch('builtins.print')
    @patch('builtins.input', return_value='Q')
    def test_q_case_insensitive(self, _input, _print):
        with self.assertRaises(SystemExit):
            _menu("Choose", ["A", "B", "C"])


class TestSelectStop(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3', '5', '1'])
    def test_multi_direction_station_returns_correct_stop(self, mock_input, _print):
        # Line 3 = Yellow, station 5 = Rosa Parks, direction 1 = Northbound
        stop_id, line = _select_stop()
        self.assertEqual(line, Line.YELLOW)
        self.assertEqual(stop_id, STOPS[Line.YELLOW]["Rosa Parks"][Direction.NORTHBOUND])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', '1'])
    def test_terminus_station_skips_direction_prompt(self, mock_input, _print):
        # Line 1 = Blue, station 1 = Hatfield Government Center (eastbound terminus only)
        stop_id, line = _select_stop()
        self.assertEqual(line, Line.BLUE)
        self.assertEqual(stop_id, STOPS[Line.BLUE]["Hatfield Government Center"][Direction.EASTBOUND])
        self.assertEqual(mock_input.call_count, 2)  # no third prompt for direction


if __name__ == "__main__":
    unittest.main()
