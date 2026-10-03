# GitHub Profile Toolkit

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/dleevn333/github-profile-toolkit)](https://github.com/dleevn333/github-profile-toolkit/releases)

> A lightweight CLI for viewing GitHub profile and repository statistics.

---

## Overview

**GitHub Profile Toolkit** is an open-source command-line tool built with Python. It queries public data from GitHub's REST API to generate a structured summary of any user's profile, including their follower metrics, total star count across public repositories, and their most-starred repository.

It has zero external package dependencies, using standard Python libraries to run anywhere effortlessly.

---

## Features

- 👤 **Profile Overview**: Displays display name, avatar URL, bio, location, followers, and following.
- 📦 **Repository Metrics**: Fetches and tallies all public repositories.
- ⭐ **Star Statistics**: Calculates the cumulative star count across all public repositories.
- 🏆 **Top Repository**: Pinpoints the user's most-starred repository with language, forks, and direct link.
- 🎨 **Elegant CLI**: Features ANSI-colored terminal cards and clean error messages.
- 🔒 **Zero Dependencies**: Uses Python's standard library (`urllib.request`, `json`, `argparse`).
- ⚡ **Rate Limit Friendly**: Supports optional `GITHUB_TOKEN` authentication to increase API limits.

---

## Installation

### Prerequisites

- Python 3.8 or higher.
- Git (optional, for cloning).

### Clone and Setup

```bash
git clone https://github.com/dleevn333/github-profile-toolkit.git
cd github-profile-toolkit
```

No external pip packages are mandatory to run the application:

```bash
python main.py --help
```

---

## Usage

### Basic Lookup

Pass any GitHub username as an argument:

```bash
python main.py torvalds
```

### Interactive Mode

Run without arguments to enter an interactive prompt:

```bash
python main.py
```

### JSON Output

Export profile and repository statistics in machine-readable JSON format:

```bash
python main.py torvalds --json
```

### Authenticated Requests (Higher Rate Limits)

To avoid GitHub's 60 requests/hour unauthenticated rate limit, you can supply a personal access token via `--token` or environment variables:

```bash
python main.py torvalds --token YOUR_GITHUB_TOKEN
# Or set in environment:
export GITHUB_TOKEN="your_personal_access_token"
```

---

## Example

Running `python main.py torvalds` produces:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
               GITHUB PROFILE TOOLKIT                 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 USER PROFILE
  Name:        Linus Torvalds (@torvalds)
  Avatar URL:  https://avatars.githubusercontent.com/u/1024025?v=4
  Location:    Portland, OR

📊 COMMUNITY & REPOSITORIES
  Followers:    260,000+
  Following:    0
  Public Repos: 12
  Total Stars:  264,000+ ⭐

⭐ TOP STARRED REPOSITORY
  Repository:  linux
  Stars:       215,000+ ⭐  |  Forks: 58,000+  |  Language: C
  URL:         https://github.com/torvalds/linux
  Description: Linux kernel source tree

──────────────────────────────────────────────────────
```

---

## Project Structure

```text
github-profile-toolkit/
├── .gitignore          # Git ignore specifications
├── LICENSE             # MIT License
├── README.md           # Documentation
├── requirements.txt    # Project requirements
├── main.py             # CLI entrypoint
├── src/
│   ├── __init__.py     # Package initialization and version
│   ├── client.py       # GitHub API client & statistics calculation
│   └── formatter.py    # ANSI color formatting & UI layout
└── tests/
    └── test_client.py  # Unit tests for the API client
```

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [Contributing Guidelines](CONTRIBUTING.md) to get started.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
