# A Git project's component

- Working tree: current state of the project incl. any changes being made 
- Staging area: changes marked to include in the next commit
- Git directory: project config + history of all file changes
- Newly created files are not tracked until `git add` is first called with it.

# Some git commands

- `git status`: get status of current brand
- `git add <file>`: add file(s) to the staging area. use `.` to incl all files in the current working dir.
- `git commit -m <commit_msg>`: commit file(s) in the staging area to the Git directory with a commit msg.

# File states
- **Modified**: made changes, not committed
- **Staged**: changes staged and **ready for the next commit** via `git add`
- **Committed**: changes committed to the Git repo via `git commit`