"""Unit tests for GitHubProfileFetcher."""

import unittest
from src.client import GitHubProfileFetcher, UserNotFoundError


class TestGitHubProfileFetcher(unittest.TestCase):
    def setUp(self):
        self.fetcher = GitHubProfileFetcher()

    def test_fetch_existing_user(self):
        result = self.fetcher.get_profile_summary("torvalds")
        self.assertEqual(result["username"].lower(), "torvalds")
        self.assertGreater(result["public_repos"], 0)
        self.assertGreater(result["total_stars"], 100000)
        self.assertIsNotNone(result["top_repository"])

    def test_fetch_non_existent_user(self):
        with self.assertRaises(UserNotFoundError):
            self.fetcher.get_profile_summary("this-user-definitely-does-not-exist-998877")


if __name__ == "__main__":
    unittest.main()
