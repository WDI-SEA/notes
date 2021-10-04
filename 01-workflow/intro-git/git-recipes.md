# Git Recipes

These are the commands for common tasks. Git can be a bit hard to memorize, since there's quite a few commands, and what those commands aren't necessarily named what you'd expect them to be named. This is intended be be a place where you can look up a task, and find the git commands needed to perform it.

## Set the git editor to something easier to use than vim

Append this to your .zshrc file:

```text
export GIT_EDITOR=pico
```

## Initialize a git repository

```text
git init
```

## Remove a git repository

```text
rm -rf .git
```

## Stage all changed file for commit

This stages the commit at that point in time. If you add more to the file after using this command, it won't be part of the commit unless you use git add again.

```text
git add . --all
```

## Unstage files

```text
git reset (file)
```

## See the status of staged files

```text
git status
```

## Commit all staged files

```text
git commit -m "(Add your commit message here)"
```

### Important note!

Committed changes get a bit harder to remove/revert. Be sure you're committing what you want to commit.

## See history of commits

```text
git log
```

## Reverse a change

Reversing a commit doesn't really undo it, it just creates another commit that changes the files you committed back to what they were before the commit. First, you have to find the ID of the commit you'd like to reverse using git log.

Copy that ID, and paste it into this command

```text
git revert (Commit ID)
```

## Destroy all changes up to a certain point

It's possible to completely remove all records of changes back to a given commit. It's not a good idea to do this on a regular basis, but rarely, it becomes necessary.

```text
git reset (Commit ID) --hard
```

If you try to push to a remote repository, the remote will just think you haven't received the latest commits, so you have to force the remote to rewrite it's own history

```text
git push origin --force
```

## Create a branch

```text
git checkout -b (branch name)
```

## Delete a branch

```text
git branch -d (branch name)
```

## Merge a branch into master

```text
git checkout master
git merge (other branch name)
```

### NOTE:

You can merge a branch into any other branch. Just check out the branch you want to merge into, then merge just like above.

```text
git checkout (branch name)
get merge (other branch name)
```

## Set remote origin

Having a repository on your computer is great, but what if other people want to contribute? Github is like a social network for git. It allows many people to work on the same repository and make commits. You have to link your local repository to Github in order to enable all this.

```text
git remote add origin (Add Github URL here)
```

## List remotes

Did we add the remote correctly? Let's find out!

```text
git remote -v
```

## Push to remote

```text
git push (remote name) (optional branch name)
```

### NOTE:

It's generally a good idea to specify which branch you're pushing. You may have a lot of local branches that your collaborators don't care about. Also, it takes more time to push every branch you may have, so usually I use

```text
git push origin master
```

in order to push only to the master branch.

## Pull from remote

```text
git pull (remote name) (optional branch name)
```

## Delete remote branch

If you do push a branch to a remote, you can delete it like this:

```text
git push origin :(branch name)
```

It's important to include the semicolon. If I had a branch named "my\_branch", I would delete it from the remote like this:

```text
git push origin :my_branch
```

