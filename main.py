#!/usr/bin/env python3
"""GitHub Profile Toolkit - CLI Entry Point."""

import argparse
import json
import sys

# Ensure UTF-8 output encoding for Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from src import __version__
from src.client import (
    GitHubAPIError,
    GitHubError,
    GitHubProfileFetcher,
    RateLimitError,
    UserNotFoundError,
)
from src.formatter import format_error, format_profile


def build_parser() -> argparse.ArgumentParser:
    """Construct command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="github-profile-toolkit",
        description="A lightweight CLI for viewing GitHub profile and repository statistics.",
        epilog="Example: python main.py torvalds",
    )
    parser.add_argument(
        "username",
        nargs="?",
        help="GitHub username to inspect (e.g., torvalds)",
    )
    parser.add_argument(
        "--token",
        "-t",
        help="GitHub Personal Access Token (defaults to GITHUB_TOKEN or GH_TOKEN env vars)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON data instead of formatted cards",
    )
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main() -> int:
    """Main execution function."""
    parser = build_parser()
    args = parser.parse_args()

    username = args.username
    if not username:
        try:
            username = input("Enter GitHub username: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled.")
            return 1

    if not username:
        print(format_error("Username cannot be empty."))
        parser.print_help()
        return 1

    fetcher = GitHubProfileFetcher(token=args.token)

    try:
        summary = fetcher.get_profile_summary(username)
    except UserNotFoundError as err:
        print(format_error(str(err)))
        return 1
    except RateLimitError as err:
        print(format_error(str(err)))
        return 1
    except (GitHubAPIError, GitHubError) as err:
        print(format_error(str(err)))
        return 1
    except Exception as err:
        print(format_error(f"Unexpected error: {err}"))
        return 1

    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print(format_profile(summary))

    return 0


if __name__ == "__main__":
    sys.exit(main())
