"""Terminal formatting and styling for GitHub Profile Toolkit."""

import os
import sys
from typing import Any, Dict


class Colors:
    """ANSI color codes for terminal styling."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"

    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright colors
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_WHITE = "\033[97m"

    @classmethod
    def supports_color(cls) -> bool:
        """Check if terminal environment supports color."""
        if os.environ.get("NO_COLOR"):
            return False
        if not hasattr(sys.stdout, "isatty") or not sys.stdout.isatty():
            return False
        return True


def colorize(text: str, color_code: str) -> str:
    """Apply ANSI color if supported, else return raw text."""
    if Colors.supports_color():
        return f"{color_code}{text}{Colors.RESET}"
    return text


def render_banner() -> str:
    """Render the tool header banner."""
    title = " GITHUB PROFILE TOOLKIT "
    line = "━" * 54
    return (
        f"\n{colorize(line, Colors.CYAN)}\n"
        f"{colorize(title.center(54), Colors.BOLD + Colors.BRIGHT_CYAN)}\n"
        f"{colorize(line, Colors.CYAN)}"
    )


def format_profile(summary: Dict[str, Any]) -> str:
    """Format the complete profile summary into an elegant CLI card."""
    lines = []
    lines.append(render_banner())

    # User Header
    name = summary.get("name") or summary.get("username")
    login = summary.get("username")
    avatar = summary.get("avatar_url") or "N/A"
    bio = summary.get("bio")
    location = summary.get("location")

    lines.append(f"\n{colorize('👤 USER PROFILE', Colors.BOLD + Colors.BRIGHT_YELLOW)}")
    lines.append(f"  {colorize('Name:', Colors.BOLD)}        {colorize(name, Colors.BRIGHT_WHITE)} (@{login})")
    lines.append(f"  {colorize('Avatar URL:', Colors.BOLD)}  {colorize(avatar, Colors.CYAN)}")
    if bio:
        lines.append(f"  {colorize('Bio:', Colors.BOLD)}         {bio.strip()}")
    if location and location != "N/A":
        lines.append(f"  {colorize('Location:', Colors.BOLD)}    {location}")

    # Metrics
    followers = summary.get("followers", 0)
    following = summary.get("following", 0)
    repos = summary.get("public_repos", 0)
    stars = summary.get("total_stars", 0)

    lines.append(f"\n{colorize('📊 COMMUNITY & REPOSITORIES', Colors.BOLD + Colors.BRIGHT_YELLOW)}")
    lines.append(f"  {colorize('Followers:', Colors.BOLD)}    {colorize(f'{followers:,}', Colors.BRIGHT_GREEN)}")
    lines.append(f"  {colorize('Following:', Colors.BOLD)}    {colorize(f'{following:,}', Colors.BRIGHT_GREEN)}")
    lines.append(f"  {colorize('Public Repos:', Colors.BOLD)} {colorize(f'{repos:,}', Colors.BRIGHT_GREEN)}")
    lines.append(f"  {colorize('Total Stars:', Colors.BOLD)}  {colorize(f'{stars:,} ⭐', Colors.BRIGHT_YELLOW)}")

    # Top Repository
    top_repo = summary.get("top_repository")
    lines.append(f"\n{colorize('⭐ TOP STARRED REPOSITORY', Colors.BOLD + Colors.BRIGHT_YELLOW)}")
    if top_repo:
        repo_name = top_repo.get("name")
        repo_stars = top_repo.get("stars", 0)
        repo_forks = top_repo.get("forks", 0)
        repo_lang = top_repo.get("language") or "N/A"
        repo_url = top_repo.get("html_url")
        repo_desc = top_repo.get("description") or "No description."

        lines.append(f"  {colorize('Repository:', Colors.BOLD)}  {colorize(repo_name, Colors.BOLD + Colors.BRIGHT_CYAN)}")
        lines.append(f"  {colorize('Stars:', Colors.BOLD)}       {colorize(f'{repo_stars:,} ⭐', Colors.BRIGHT_YELLOW)}  |  {colorize('Forks:', Colors.BOLD)} {repo_forks:,}  |  {colorize('Language:', Colors.BOLD)} {repo_lang}")
        lines.append(f"  {colorize('URL:', Colors.BOLD)}         {colorize(repo_url, Colors.CYAN)}")
        lines.append(f"  {colorize('Description:', Colors.BOLD)} {repo_desc}")
    else:
        lines.append(f"  {colorize('No public repositories found.', Colors.DIM)}")

    divider = "─" * 54
    lines.append(f"\n{colorize(divider, Colors.DIM)}\n")
    return "\n".join(lines)


def format_error(message: str) -> str:
    """Format an error message with distinct red styling."""
    prefix = colorize("✖ ERROR:", Colors.BOLD + Colors.RED)
    return f"\n{prefix} {colorize(message, Colors.RED)}\n"
