![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#Intro to Git

## Objectives

* Define version control systems
* Identify main git commands to manage files
* Distinguish bewteen local and remote repositories

## Motivation

Have you ever worked on a paper or any document collaboratively with others?

* What have you noticed?
* What was the workflow like?
* What did work, what didn't?

Now enter software programming. Programming is a highly team based activity. That's why I love programming: A project is always more fun when you've got friends working with you. Sometimes very large teams work on a single project. We as developers need tools that support collaborative working. Enter **Version Control Systems**.

## What is version control, and why should you care?

So how do you collaborate in software projects?

In the most fundamental way, version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

More specifically, a VCS allows you to:

* revert files back to a previous state
* revert the entire project back to a previous state
* review changes made over time
* collaborate on a set of files with others
* see who last modified something that might be causing a problem

Plus it functions as a backup system, a safe place for all your work. Using a VCS means that if you screw things up or lose files, you can generally recover easily. In addition, you get all this for very little overhead.

There are many VCS. Git and GitHub have become the VCS of choice for most software teams. Do you know other VCS?

# Definitions

Git and github provide a framework, tools and workflows for collaboration.

## git

  git is a version control system

## Github

Is a social network build around git. It has completely changed the way we, as programmers, work. GitHub is now the largest online storage space of collaborative works.

  git and github together is a **distributed** version control system

![DVCS diagram](http://git-scm.com/figures/18333fig0103-tn.png)

We're going to talk about git first. git is local (Computer A), that's your laptop. Nearly every operation is local. Most operations in Git only need local files and resources to operate - generally no information is needed from another computer on your network.

Github is the "Server Computer".

## Folder Management

A word about folder management.

Recommendation: Create "Code" folder in your home directory. This is the place for all source code that you create at GA (projects, labs, homework). Let's talk about folder structure.

Options:

* By time
* By topic
* A combination of both

Discuss approach. What works for you? I recommend that you decide on a structure in the first week and stick to it. We found that organizing folders by time works for most.

**1) Let's get started and create a project with a single file**

Create file that contains your name and contact info. Example:

  `~/Code/week0/project_git/my_contact.txt`

**2) Create a git repository**

First, `cd` into project_git folder.

The first step is creating a version database, i.e. a repository

  `git init`

You do this only once per project. Let's check the status of our newly created repo:

  `git status`

**3) Let's put it under git management**

You can add files individually or the entire directory, including sub folders.

    git add my_contact.txt

    git add . (adds everything in the current folder)

The file is now **tracked** by git. Run `git status` to see for yourself.

**4) Add file to git repository**

Let's say you're happy with your work and want to save a version. This is called **committing**:

    git commit -m 'my first commit' my_contact.txt

    git commit -m 'my first commit . (commits everything in the current folder)

The file now has a unique version in git and can be recovered if lost. Make sure everything is *clean*:

    git status

**5) Let's make changes**

Go add a line to the contacts file, or make any change, and save. Then run:

    git status my_contact.txt

How do we find out what changed?

    git diff my_contact.txt

We're happy with the changes, so let's commit:

    git commit -m 'added phone number' .

**6) Discard changes**

What if you make an unwanted change and want to unmodify a file?

    git checkout my_contact.txt

Note that once you make a commit, you won't be able to unmodify those files. You can see a list of your commits by running:

    git log

**7) Recover work**

Now lets blow everything away!

    rm *.*

And get it back

    git checkout .

**8) Deleting files**

Let's delete a file for good

    git rm <file>
    git commit -a -m'deleted file'

**To summarize**

* `git add` files that become part of your program (track)
* `git status <file>` or `.` to see which files changed.
* `git diff` to see exactly what changed (by line)
* `git commit` files I'm happy with with (commit)
* `git checkout` to dicsard local changes (unmodifiy)

This is the most simple workflow, things get a bit more complex when you start sharing code and manage larger code bases. But this is a good start.

**Note (important): Avoid creating git repositories inside other git repositories.**

**Resources**

[Git](http://git-scm.com/book/en)
