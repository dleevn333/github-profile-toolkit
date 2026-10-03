"""GitHub API client for fetching profile and repository statistics."""

import json
import os
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional


class GitHubError(Exception):
    """Base exception for GitHub API errors."""
    pass


class UserNotFoundError(GitHubError):
    """Raised when the specified GitHub user does not exist."""
    def __init__(self, username: str):
        super().__init__(f"GitHub user '{username}' was not found (404).")
        self.username = username


class RateLimitError(GitHubError):
    """Raised when GitHub API rate limit is exceeded."""
    def __init__(self, message: str = "GitHub API rate limit exceeded."):
        super().__init__(message)


class GitHubAPIError(GitHubError):
    """Raised when GitHub API returns an unexpected error."""
    def __init__(self, status_code: int, message: str):
        super().__init__(f"GitHub API Error [{status_code}]: {message}")
        self.status_code = status_code


class GitHubProfileFetcher:
    """Client to query public GitHub user profile and repositories."""

    BASE_URL = "https://api.github.com"

    def __init__(self, token: Optional[str] = None):
        """Initialize with an optional GitHub personal access token."""
        self.token = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    def _make_request(self, endpoint: str) -> Any:
        """Make an authenticated or unauthenticated HTTP GET request to GitHub API."""
        url = f"{self.BASE_URL}/{endpoint.lstrip('/')}"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "github-profile-toolkit/1.0.0",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        req = urllib.request.Request(url, headers=headers, method="GET")

        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                payload = response.read().decode("utf-8")
                return json.loads(payload)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                raise UserNotFoundError(endpoint.split("/")[1] if "users/" in endpoint else endpoint)
            elif err.code in (403, 429):
                # Check for rate limit
                rate_remaining = err.headers.get("X-RateLimit-Remaining")
                if rate_remaining == "0" or "rate limit" in str(err.reason).lower():
                    raise RateLimitError(
                        "GitHub API rate limit exceeded. Set GITHUB_TOKEN environment variable to increase limit."
                    )
                raise GitHubAPIError(err.code, err.reason)
            else:
                try:
                    error_data = json.loads(err.read().decode("utf-8"))
                    err_msg = error_data.get("message", err.reason)
                except Exception:
                    err_msg = err.reason
                raise GitHubAPIError(err.code, err_msg)
        except urllib.error.URLError as err:
            raise GitHubError(f"Network connection error: {err.reason}")

    def fetch_user_profile(self, username: str) -> Dict[str, Any]:
        """Fetch profile information for a GitHub user."""
        clean_user = username.strip()
        if not clean_user:
            raise ValueError("Username cannot be empty.")
        return self._make_request(f"users/{clean_user}")

    def fetch_user_repositories(self, username: str, max_repos: int = 100) -> List[Dict[str, Any]]:
        """Fetch public repositories for a GitHub user (up to max_repos)."""
        clean_user = username.strip()
        if not clean_user:
            raise ValueError("Username cannot be empty.")

        repos: List[Dict[str, Any]] = []
        page = 1
        per_page = min(max_repos, 100)

        while len(repos) < max_repos:
            endpoint = f"users/{clean_user}/repos?per_page={per_page}&page={page}&type=owner&sort=updated"
            batch = self._make_request(endpoint)
            if not batch:
                break
            repos.extend(batch)
            if len(batch) < per_page:
                break
            page += 1

        return repos[:max_repos]

    def get_profile_summary(self, username: str) -> Dict[str, Any]:
        """Fetch user profile and calculate repository & star statistics."""
        user_data = self.fetch_user_profile(username)
        repos_data = self.fetch_user_repositories(username)

        total_stars = sum(repo.get("stargazers_count", 0) for repo in repos_data)

        top_repo = None
        if repos_data:
            sorted_repos = sorted(repos_data, key=lambda r: r.get("stargazers_count", 0), reverse=True)
            best = sorted_repos[0]
            top_repo = {
                "name": best.get("name"),
                "full_name": best.get("full_name"),
                "stars": best.get("stargazers_count", 0),
                "forks": best.get("forks_count", 0),
                "language": best.get("language") or "N/A",
                "html_url": best.get("html_url"),
                "description": best.get("description") or "No description provided.",
            }

        return {
            "username": user_data.get("login"),
            "name": user_data.get("name") or user_data.get("login"),
            "avatar_url": user_data.get("avatar_url"),
            "bio": user_data.get("bio") or "",
            "location": user_data.get("location") or "N/A",
            "company": user_data.get("company") or "N/A",
            "blog": user_data.get("blog") or "N/A",
            "followers": user_data.get("followers", 0),
            "following": user_data.get("following", 0),
            "public_repos": user_data.get("public_repos", 0),
            "total_stars": total_stars,
            "top_repository": top_repo,
        }
