# Git Basics (Quick Reference)

## Mental Model
- Git tracks changes using snapshots called commits
- GitHub stores those commits online
- Changes flow: working directory → staging → commit → push

---

## Core Areas
- Working directory: files I am editing
- Staging area: changes selected for the next commit
- Commit history: saved snapshots
- Remote (GitHub): uploaded commit history

---

## Common Commands
git add .       (stage all changes for next commit)
git add file.py         (stages only for a specific file)
git commit -m "Describe what changed"       (creates a single snapshot in local history.)
git push        (push all commits to github)



### Check status
git status (Shows what files are changed, staged, or untracked.)
