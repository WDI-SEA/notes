#Local Git Repo

A git repo is represented by a directory, just like any project. All your files will go in a directory. Try creating a directory with the following files:

- project_git
  - readme.md

Once you're done, we can start on the first git command.

## `git init` - Creating a local git repo

Inside the folder, you'll want to run the following command.

```
git init
```

This command will initialize a git repo, which actually creates a hidden folder that stores all the changes made to the project.

You'll only need to do this once per project. If you're cloning a git repo, this step is already taken care of for you.

## `git status` - Checking your repo status

```
git status
```

Think of `git status` as your dashboard. The command will show you everything you need to know about the current state of your git repo, from untracked files to any outstanding changes that need to be made.

Currently, there are no commits, so we'll want to put files under the management of git. It'll involve two steps, **adding** and **committing**. These steps are very different.

## `git add` - Adding files and directories

You can add files individually or the entire directory, including subfolders.

```
git add readme.md
git add .
```

The second command will add everything in the current working directory. But try running `git status` again. While the `git add` command adds these file changes, they're not actually saved. Think of this as the "staging" area of files where we decide what to permanently save and what to discard. Another good way to think of this is in baseball terms. This staging area is the "on-deck circle", getting things ready before batting.

## `git commit` - Saving staged files

Let's say you're happy with your work and want to save a version. This is called **committing**:

```
git commit -m 'my first commit'
```

Now, the changes are permanently saved. The file now has a unique version in git and can be recovered if lost. Make sure everything is *clean* by running `git status` again.

## Process for making changes

#### File status

Try making changes to the `readme.md` file. See what happens when you run:

```
git status
```

#### `git diff` - file differences

How do we find out what changed?

```
git diff readme.md
```

#### Stage and save

When we're ready to save those changes

```
git add readme.md
git commit -m 'added title'
```

#### `git checkout` - checkout changes

Or, we can undo changes. If changes have been made before comitting, we can run `checkout` to reset the file back to its most recent commit state.

```
git checkout readme.md
```

#### `git log` - review commit history

Note that once you make a commit, you won't be able to unmodify those files. You can see a list of your commits by running:

```
git log
```

#### `git rm` - untrack a file

If a file has been added to git and it needs to be deleted, we can run `git rm` and commit the change.

```
git rm <file>
git commit -am 'deleted file'
```

## Summary

* `git add` files that become part of your program (track)
* `git status <file>` or `.` to see which files changed.
* `git diff` to see exactly what changed (by line)
* `git commit` file changes to save (commit)
* `git checkout` to dicsard local changes (unmodifiy)
* `git rem` to untrack files (remove)

This is the most simple workflow, things get a bit more complex when you start sharing code and manage larger code bases. But this is a good start.

**IMPORTANT NOTE: Avoid creating git repositories inside other git repositories.**
