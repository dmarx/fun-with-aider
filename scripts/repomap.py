# scripts/repomap.py
"""
See also: https://github.com/Aider-AI/aider/blob/main/aider/repomap.py
"""
import aider
from aider.io import InputOutput
from aider.repomap import RepoMap
from pathlib import Path

all_files = Path(".").rglob("*") # NB: this object is a generator, not a materialized list
#print(f"all_files: {all_files}")

io = InputOutput()
map = RepoMap(io=io)
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
#repo_content = map.get_ranked_tags_map(chat_fnames=all_files, force_refresh=True) # NoneType not iterable
# all_files = list(all_files)
#print(f"all_files: {all_files}")
#repo_content = map.get_ranked_tags_map(chat_fnames=all_files, force_refresh=True) # self.io.tool_warning(f"Repo-map can't include {fname}")
#all_files = [str(f.absolute()) for f in all_files]
all_files = [str(f.absolute()) for f in all_files if f.is_file()]
all_files = [f for f in all_files if not any([bad in f for bad in (".git",".aider")])]
print(all_files)
#repo_content = map.get_ranked_tags_map(chat_fnames=all_files, force_refresh=True) # fails without a `main_model` to query max token count for
#repo_content = map.get_ranked_tags(chat_fnames=all_files, other_fnames=list(), mentioned_fnames=set(),mentioned_idents=set(),) # fails because of missing self.io attribute. with io, it's just the one file that has a function defined (which is not only python script). and no information about that file, just it's name.
repo_content = map.get_ranked_tags_map_uncached(chat_fnames=all_files)
print(repo_content)
