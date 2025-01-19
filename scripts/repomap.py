# scripts/repomap.py
"""
See also: https://github.com/Aider-AI/aider/blob/main/aider/repomap.py
"""
import aider
from aider.repomap import RepoMap
from pathlib import Path

all_files = Path(".").glob("*") # NB: this object is a generator, not a materialized list
#print(f"all_files: {all_files}")

map = RepoMap()
# repo_content = map.get_repo_map(chat_files=None, other_files=None)
# print(repo_content) # None
# repo_content = map.get_repo_map(chat_files=all_files, other_files=None)
# print(repo_content) # None
# repo_content = map.get_repo_map(chat_files=all_files, other_files=all_files) # ZeroDivisionError
# print(repo_content)
#all_files = list(all_files)
#repo_content = map.get_repo_map(chat_files=all_files, other_files=None)
#print(repo_content)
#repo_content = map.get_repo_map(chat_files=all_files, other_files=all_files)
#print(repo_content)


#repo_content = map.get_ranked_tags_map(chat_fnames=None, force_refresh=True) # NoneType not iterable
repo_content = map.get_ranked_tags_map(chat_fnames=all_files, force_refresh=True) # NoneType not iterable
print(repo_content)
