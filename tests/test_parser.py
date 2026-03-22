import unittest
import sys
sys.path.insert(0, '..')

from parser import parse_log, filter_errors, filter_by_user
from reporter import get_error_summary, get_user_summary

class TestParser(unittest.TestCase):

    def setUp(self):
        """Runs before every test — loads the log file once."""
        self.logs = parse_log('sample_logs/syslog.log')

    def test_parse_returns_list(self):
        """parse_log should return a list."""
        self.assertIsInstance(self.logs, list)

    def test_parse_returns_dicts(self):
        """Each entry should be a dict with correct keys."""
        for entry in self.logs:
            self.assertIn('code', entry)
            self.assertIn('message', entry)
            self.assertIn('user', entry)

    def test_filter_errors_only_returns_errors(self):
        """filter_errors should return only ERROR entries."""
        errors = filter_errors(self.logs)
        for entry in errors:
            self.assertEqual(entry['code'], 'ERROR')

    def test_filter_by_user_returns_correct_user(self):
        """filter_by_user should return only entries for that user."""
        results = filter_by_user(self.logs, 'blossom')
        for entry in results:
            self.assertEqual(entry['user'], 'blossom')

    def test_filter_by_unknown_user_returns_empty(self):
        """filter_by_user with unknown user should return empty list."""
        results = filter_by_user(self.logs, 'nobody')
        self.assertEqual(results, [])

    def test_error_summary_sorted_by_count(self):
        """get_error_summary should return errors from most to least."""
        summary = get_error_summary(self.logs)
        counts = [count for _, count in summary]
        self.assertEqual(counts, sorted(counts, reverse=True))

    def test_user_summary_sorted_alphabetically(self):
        """get_user_summary should be sorted by username."""
        summary = get_user_summary(self.logs)
        usernames = [user for user, _, _ in summary]
        self.assertEqual(usernames, sorted(usernames))


if __name__ == '__main__':
    unittest.main(verbosity=2)