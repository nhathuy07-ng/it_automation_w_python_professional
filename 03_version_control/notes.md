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

## Branching

- `git branch branch-name`: create new branch, but DOES NOT transition to this branch
- `git checkout branch-name`: change worktree to the latest snapshot of the target branch `branch-name`
- `git checkout -b branch-name`: create new branch, then change worktree to latest snapshot of the target branch `branch-name` 
- `git branch -d branch-name`: deletes branch `branch-name`

## Merging changes

- `git merge branch-name`: merge branch `branch-name` to the current branch:
    - fast-forward merging: when there's no new commits on original branch since the new branch is created.
    - three-way merging:
        - When there are new commits on original branch since the new branch is created.
        - Three-way merging done based on common ancestor of the two branches. 
        - If the same part of the file is modified on both branches, a **merge conflict** occur.

### `git fetch` vs `git remote update`

- `git fetch <remote>`: fetches updates from the current or default remote only, usually `origin`
- `git remote update`: fetches updates from all configured remotes at once.

## Rebasing changes

- Changing the base of the branch history by replaying them on top of the new base (i.e the HEAD of the chosen branch to rebase on)

- Simply put, rebasing lifts the commits off their common ancestor with the chosen branch and replays them on the HEAD of that branch.

```plaintext
Before Rebase:
      A---B---C (feature)
     /
D---E---F---G (main)

After Rebase:
              A'--B'--C' (feature)
             /
D---E---F---G (main)
```

- Do this if a linear commit history is desired, for example, in case we want to trace which commit initially caused problems (if any) in our project.

- Command: `git rebase <branch>`

> [!IMPORTANT]
> Never rebase shared branches, because doing so "rewrites" the branch history, and Git servers rejects pushes that alter the remote history. If you force the change, anyone working on that branch can encounter severe merge conflicts on their next pulls.

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

# Collaborating on Git

## Making a pull request (PR).

> This should be simple enough.

## Updating existing PRs:

- Each pull request is pointed to a branch. Just make changes in that branch, commit & push the changes to the remote repo. The commit will be included in the same PR.

- To create a new PR, create a new branch.

## Squashing changes

- Meld the selected commit with the previous one.

- Use `git rebase -i <remote>` for interactive rebasing (incl. squashing and other ops).

- If rewriting history is needed (i.e, due to squashing commits, should be done in personal PRs only), use `git push -f` to force push the current snapshot to the repo.