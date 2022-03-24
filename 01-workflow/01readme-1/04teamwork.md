# Git and Team Workflow Cheatsheet

## Team Workflow

To help illustrate collaborating on a project using Git/GitHub, consider the following two roles you can fulfill: **programmer** and **manager**.

**Programmers** will contribute code and issue pull requests, while **managers** integrate the code by merging the pull requests into the repo.

### Creating the Repo (One-time Setup)

**Manager**:

1. Create a repo locally, using `$ git init`.
2. Create a remote version of this repo on GitHub (using `hub create` if
   you wish).
3. Ensure you have a remote named **origin**: `$ git remote -v`

**Programmer**:

1. **Identify the repo created by your manager** on GitHub.
2. **Fork the repo** to your own account.
3. Use `$ git clone <link to your repo>` to **copy your forked repo locally**. Obtain the link to your repo by clicking the green "Clone or download" button.
4. **`cd`** into the newly created project folder.
5. Now **add a link to the manager's repo** as well: `$ git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git`
6. **Ensure that you have two remote links** named `origin` & `upstream`: `$ git remote -v`
7. **Ensure you are notified of changes to the project** by clicking the **Watch** button near the top right of the manager's repo.  Then make sure you GitHub account's notification settings are adjusted to notify you via email, etc.

### Working on Feature Branches

<img src="https://i.imgur.com/B5CZSuT.png">

**Manager** & **Programmer**:

1. Frequently **ensure that you have the most recently merged code** on your local computer:
	- Checkout the `main` branch with `git checkout main`. *Only
   pull when you are on `main`.*
	- Now you can `$ git pull upstream main`. **Managers** will always use `origin` in place of `upstream`.
2. **Use a feature branch** with `$ git checkout <feature_branch_name>`;
   add `-b` to create a new branch if necessary. Name the branch after the feature you are working on implementing in that branch.  **You should never write code while in the `main` branch**.
3. Write some code!
4. **When you have completed a feature:**
	- Commit your code as usual...
   	- `$ git push origin <feature_branch_name>`
5. On **your** GitHub repo's page, find and click the Pull Request button.
6. FYI, multiple commits are grouped within a single open pull request.
7. Go back to step #2.

### Accepting and Merging A Pull Request

**Manager**:

1. If GitHub states that the pull request can be merged automatically - do it!
2. If GitHub states there will be conflicts, and the merge is smallish, it is still possible to merge online by following the instructions.
3. If the request is very comprehensive and may cause plenty of merge conflicts, the manager may decide to test and merge the pull request locally/manually by clicking **command line instructions** and following the steps listed.
4. After a merge, ensure your team members pull the recent changes into their local repo ASAP.

### Minimizing Merge Conflicts

1. Try to divide up work so that programmers don't make changes to the same file between merges. 
2. When notified that branches have been merged into `main` by the manager, **immediately** bring your local repo up to date so that you are working with the latest and greatest:
	- We're going to need to checkout the main branch to update it, however, _sometimes_ Git will not allow us checkout a different branch if there are uncommitted changes in the current branch.  The solution is to either `stash` or `commit` the changes first. Please read [this StackOverflow](https://stackoverflow.com/questions/22053757/checkout-another-branch-when-there-are-uncommitted-changes-on-the-current-branch) for how to resolve this scenario if Git does not allow the next step (`$ git checkout main`).
	- `$ git checkout main`
	- `$ git pull upstream main` **Manager** uses `origin` instead of `upstream`
	- `$ git checkout <feature_branch_name>`
	- `$ git merge main` This brings the latest code into your feature branch so that you are always developing with the latest and greatest.
3. Making frequent and small commits and pull requests will help minimize merge conflicts.

### Fixing Merge Conflicts Locally (especially for programmers)

>Note: When merging the latest and greatest into your feature branch, it's possible to create merge conflicts too. So managers aren't the only ones who get to enjoy fixing merge conflicts!

1. You will/should be in your feature branch when the conflicts occurred.
2. Typing `$ git status` will show you which file(s) have conflicts.
3. You will need to edit those files to remove the markers and fix up the code to what it "should" be - if in doubt what, consult your manager or other teammates.
4. After fixing the commits:
	- `$ git add -A`
	- `$ git commit -m "Fix merge conflicts"`
5. Continue developing as usual.

### Checking the Logs

To visualize the history of commits made to the repo we use the `git log` command. There are several options, but this format works well:

`$ git log --decorate --graph --oneline`

---

## Git Command Reference

#### Creating Repos

- **`$ git init`** Initializes a new local repository and begins version
  tracking. Creates a hidden directory that tracks info about the repository,
  including remote repositories.
- **`$ git clone <ssh_or_http_url>`** Clones a remote repository as a new local
  repository with the given connection format (SSH or HTTPS).
- **`$ git remote add <remote_name> <ssh_or_http_url>`** Connects your repo to
  a new remote at the given URL, via the given connection format
  (SSH or HTTPS), and names it with the given name.

#### Working on Repos

##### Branching and Merging

- **`$ git branch <branch_name>`** Creates a new branch with the given name.
- **`$ git checkout <branch_name>`** Moves you to the branch (or commit in
  history) with the given name.
- **`$ git checkout - b <branch_name>`** Creates a new branch and checks it
  out, all in one!
- **`$ git merge <branch_name>`** Merges the branch cwith the given name into
  the current branch.

##### Staging Changes

- **`$ git add <file_name>`** Adds changes made to the given file to 
  the staging area.
- **`$ git add .`** Adds all changes (creating, updating and removing files),
  to files in this directory and sub-directories, to the staging area.
- **`$ git add -A`** Adds all changes (creating, updating and removing files),
  in all files, to the staging area.
- **`$ git add -p`** Adds updates in all staged files to the staging area,
  but runs you through all the changes step by step.

##### Committing Snapshots

- **`$ git commit -m "awesome commit message"`** Saves a snapshot of the
  filesystem including any changes that have been added/staged as a commit.
  It saves the commit with a simple description, or *message*, given after
  `-m`.
- **`$ git commit`** Commits as above, but takes you to a text editor (`nano`)
  to edit the commit's *message*.

##### Exploring Repos

- **`$ git status`** Prints out the current "tracking state" of the repo. The
  state includes information about changes, additions and deletions of
  files, whether or not these changes have been added/stages, and sometimes
  even any merge conflicts.
- **`$ git log`** Prints out the commit history of the current branch of the
  current repo.
- **`$ git branch` & `$ git branch -v`** Prints out a list of all available
  branches in the repo.
- **`$ git remote` & `$ git remote -v`** Prints out a list of all available
  bremotes connected to the repo.
- **`$ git diff <branch_or_commit_name>`** Prints out information about
  *differences*, as insertions (in green) and deletions (in red), between
  the current commit and the given commit (or the most current commit in the
  given branch).

#### Collaborating with Other Repos (Remotes)

- **`$ git push (-u) (<remote_name> <branch_name>)`** Push, or send, commits to
  remote at the given branch. `-u` saves the remote and branch names as
  default for future use.
- **`$ git fetch <remote_name> <branch_name>`** Fetch, or receive, commits from
  a given remote at the given branch. Stores these commits in either the
  named commit, or in a special, new branch.
- **`$ git pull <remote_name> <branch_name>`** Performs a `git fetch` into a new
  branch, then merges it into the current branch and removes the fetched
  branch.

## Resources

Articles and tutorials on branching and workflows in Git:

- [Git Branching][atlassian-branches]
- [Common Git Workflows][atlassian-workflows]
- [In-depth Discussion of a Workflow][in-depth-workflow]
- ['Reset Demystified'][git-scm-blog-reset] (helps to understand the structures of Git)
- **[A Git Branching visualization game!][git-viz-game]**

<!-- Links -->

[repo-image]: assets/git-workflow-1.png

[branching-deck]:         https://docs.google.com/presentation/d/1tE0D8F-TNNG36tjCN-H1hzhjAb2rWknGcohEESaPW08/edit#slide=id.p
[atlassian-branches]:     https://www.atlassian.com/git/tutorials/using-branches
[atlassian-workflows]:    https://www.atlassian.com/git/tutorials/comparing-workflows
[in-depth-workflow]:      http://nvie.com/posts/a-successful-git-branching-model
[git-scm-blog-reset]:     https://git-scm.com/blog/2011/07/11/reset.html
[git-viz-game]:           http://pcottle.github.io/learnGitBranching

[local-merge]: https://help.github.com/articles/checking-out-pull-requests-locally/#modifying-an-inactive-pull-request-locally
[pr]:          https://help.github.com/articles/creating-a-pull-request


