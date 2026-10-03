# GitHub Profile Toolkit

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/dleevn333/github-profile-toolkit)](https://github.com/dleevn333/github-profile-toolkit/releases)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)

> A lightweight, zero-dependency Python CLI for exploring GitHub profiles, public repository analytics, and community star metrics.

---

## Quick Start (< 30 seconds)

```bash
# 1. Clone repository
git clone https://github.com/dleevn333/github-profile-toolkit.git
cd github-profile-toolkit

# 2. Run instant lookup (no pip installs needed!)
python main.py torvalds
```

---

## Why Use This?

- ⚡ **Zero External Dependencies**: Works out-of-the-box on standard Python 3.8+ using built-in libraries (`urllib`, `json`, `argparse`).
- 🔓 **No API Token Required**: Fetches public statistics immediately without requiring mandatory authentication.
- ⭐ **Aggregated Star Metrics**: Automatically calculates cumulative stars across public repositories.
- 🏆 **Multi-Repo Analytics**: Discover top repositories ranked by stars or forks with `--top N`.
- 💻 **Cross-Platform Formatting**: Beautiful ANSI terminal cards with automatic UTF-8 fallback on Windows Command Prompt and PowerShell.
- 🤖 **Automation Ready**: Output structured JSON directly via `--json` for scripts, CI/CD, or webhooks.

---

## Features

- 👤 **Profile Overview**: Displays display name, avatar URL, bio, location, followers, and following.
- 📦 **Repository Metrics**: Fetches and tallies all public repositories.
- ⭐ **Star Statistics**: Calculates total stars across all public repositories.
- 🏆 **Top Repositories**: Highlights the user's highest-impact projects sorted by stars or forks.
- 🎨 **Elegant CLI**: Features ANSI-colored terminal cards and clean error messages.
- 🔑 **Rate Limit Friendly**: Supports optional `GITHUB_TOKEN` authentication to boost API limits from 60 to 5,000 requests/hr.

---

## Terminal Demo

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                GITHUB PROFILE TOOLKIT                
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👤 USER PROFILE
  Name:        Linus Torvalds (@torvalds)
  Avatar URL:  https://avatars.githubusercontent.com/u/1024025?v=4
  Location:    Portland, OR

📊 COMMUNITY & REPOSITORIES
  Followers:    326,072
  Following:    0
  Public Repos: 12
  Total Stars:  264,263 ⭐

⭐ TOP REPOSITORIES
  [1] Repository:  linux
      Stars:       250,911 ⭐  |  Forks: 66,549  |  Language: C
      URL:         https://github.com/torvalds/linux
      Description: Linux kernel source tree
      · · ·
  [2] Repository:  AudioNoise
      Stars:       4,514 ⭐  |  Forks: 224  |  Language: C
      URL:         https://github.com/torvalds/AudioNoise
      Description: Random digital audio effects
      · · ·
  [3] Repository:  GuitarPedal
      Stars:       2,415 ⭐  |  Forks: 121  |  Language: C
      URL:         https://github.com/torvalds/GuitarPedal
      Description: Linus learns analog circuits

──────────────────────────────────────────────────────
```

---

## Installation

### Prerequisites

- Python 3.8 or higher.
- Git (optional, for cloning).

### Setup

```bash
git clone https://github.com/dleevn333/github-profile-toolkit.git
cd github-profile-toolkit
```

No external pip packages are mandatory to run the application:

```bash
python main.py --help
```

---

## Usage Guide

### 1. Basic Profile Lookup
```bash
python main.py torvalds
```

### 2. View Top N Repositories
View top 3 or 5 repositories instead of just the first:
```bash
python main.py torvalds --top 3
```

### 3. Sort by Forks
Sort top repositories by fork count instead of stars:
```bash
python main.py torvalds --top 3 --sort forks
```

### 4. Interactive Mode
Run without arguments to launch the interactive prompt:
```bash
python main.py
```

### 5. Machine-Readable JSON Export
Export data for scripting or piping to `jq`:
```bash
python main.py torvalds --json
```

### 6. Authenticated Requests
To bypass GitHub's 60 req/hr unauthenticated limit:
```bash
# Pass via argument
python main.py torvalds --token YOUR_GITHUB_TOKEN

# Or export in your shell
export GITHUB_TOKEN="ghp_your_token_here"
python main.py torvalds
```

---

## Troubleshooting

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| `✖ ERROR: GitHub API rate limit exceeded` | GitHub limits unauthenticated requests to 60/hr per IP. | Set `GITHUB_TOKEN` environment variable or use `gh auth login` to get 5,000 requests/hr. |
| `✖ ERROR: GitHub user '...' was not found (404)` | Username misspelled or account deleted/renamed. | Verify the username exists on `https://github.com/<username>`. |
| Windows Terminal Encoding Issues | Legacy Windows Command Prompt (`cmd.exe`) code page. | Run `chcp 65001` before executing or use Windows Terminal (UTF-8 enabled by default in Python 3.7+). |

---

## Project Structure

```text
github-profile-toolkit/
├── .gitignore          # Git ignore specifications
├── LICENSE             # MIT License
├── README.md           # Documentation
├── CONTRIBUTING.md     # Contribution guidelines
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
