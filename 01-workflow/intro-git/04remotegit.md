#Remote Git Repo

In the previous section, we worked with a local git repo. Now, let's try working with a remote repo, and clone it to create a local repo.

## Setup for this section

* Create a new repo on Github (we'll use `tacos` for ours)

## Working with Remote Repositories

We previously mentioned that git is a **distributed version control system**. Meaning, we can make changes locally, and push them up to a server. We can also pull down changes from a server. Throughout WDI, we'll be working with remote repositories mainly through Github in order to submit deliverables. So let's go through an example.

## `git clone` - clone a repository

If you have your own repo on Github, you'll likely want to make changes on your local computer. In order to do this, you'll want to **clone** the repository, which creates a copy of a repo. The syntax will require the SSH URL.

```
git clone <SSH URL GOES HERE>
```

Once this is done, you'll have a copy on your local machine. No need to run `git init` or anything, it's all done for you!

## `git pull` - pull changes from Github

Now that you have a local copy of the repo, if any changes are made on Github, you can pull those changes down by running a pull command.

```
git pull
```

Try making a change on Github using the built-in GUI and run this command! You'll see that the changes will be pulled down.

## `git push` - push changes to Github

Similarly, if we make changes to our local copy of the repo, we can push those changes to Github by running a push command.

```
git push
```

Try making a change locally, add your changes, and commit your changes. Run this command, and you'll see that the changes will be pushed to Github.

## `git remote` - how git knows your remotes

How does `git pull` and `git push` work? Git uses a list of *remotes* to know where to push and pull from. You can view a list of these remotes by running the remote command:

```
git remote -v
```

By default, cloning your Github repo will create remotes for pushing and pulling, via the SSH URL. We'll be using these in the future for more complex pushing and pulling.

## Forking - Github's way to share and collaborate

When we work on deliverables in WDI and in the software industry, we'll usually be building upon pre-existing scaffolds or projects. In these cases, we'll usually want our own copies to work on, because the project owner won't allow you to make direct changes. Otherwise chaos would ensue!

The solution is to create a **fork** of a repo. It's kinda like a clone, but it's all done on Github and gives you ownership of the copy. You'll then make changes in this fork.

Once you want to officially submit your changes, you'll perform what's called a **pull request**, which we'll demo before your first deliverable.
