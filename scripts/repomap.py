# scripts/repomap.py
"""
See also: https://github.com/Aider-AI/aider/blob/main/aider/repomap.py
"""
import aider
from aider.repomap import RepoMap
from pathlib import Path

all_files = Path(".").glob("*")
print(f"all_files: {all_files}")

map = RepoMap()
repo_content = map.get_repo_map(chat_files=None, other_files=None)
print(repo_content)
