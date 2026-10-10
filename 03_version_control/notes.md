# A Git project's component

- Working tree: current state of the project incl. any changes being made 
- Staging area: changes marked to include in the next commit
- Git directory: project config + history of all file changes
- Newly created files are not tracked until `git add` is first called with it.

# Some git commands

## Initialize repo, stage and commit changes
- `git init`: create a new git repo in the CWD
- `git status`: get status of current brand
- `git add <file>`: add file(s) to the staging area. use `.` to incl all files in the current working dir.
- `git commit -m <commit_msg>`: commit file(s) in the staging area to the Git directory with a commit msg.
- `git commit -a`: commit **tracked** file(s) without staging them. does not do anything with untracked files (those need to be `add`ed first)

## View past commits & changes
- `git log`: see list of commits w/ basic metadata
- `git log -p`: see list of commits with detailed changes for each commit
- `git log --stat`: see list of commits w/ number of files changed, insertions and deletions.
- `git show <id>`: show changes by commit ID
- `git diff`: show changes to tracked but unstaged files compared to staged.
- `git diff --staged`: show changes in staging compared to HEAD.

## Amend commits
- `git commit --amend` to perform changes (file changes and commit message) to the most recent commit. Works by amending changes in the staging area to the most recent commit. Should NOT be used on public commits (w/ multiple collaborators).

- `git revert HEAD`: creates a new commit that cancels out changes in the most recent commit.
- `git revert <commit-hash>`: same thing, but for a particular commit

> [!IMPORTANT]
> If later commits modified, moved or deleted the exact same lines of code in the commit-to-be-reversed, **conflict occurs**. Git will pause the operation, marks the conflicting files and leaves conflict markers in the code.

# File states
- **Modified**: made changes, not committed
- **Staged**: changes staged and **ready for the next commit** via `git add`
- **Committed**: changes committed to the Git repo via `git commit`

# Anatomy of a commit msg

- Commit ID: SHA1 hash (40 chars) from commit date, author, snapshot of working tree => Each time a commit is **amended**, commit ID is **rehashed**.
    - To identify a commit, you often only need to type the first n characters of an ID, provided that that string of numbers is unique to one commit.

- Short description of the change (up to 50 chars)
- <Blank line>
- Details of changes (if relevant). Up to 72 chars/line.
    - What changed? Why?
    - Issues/tickets resolved?
    - etc.
