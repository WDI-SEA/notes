# Version Control

## What is version control, and why should you care?

Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. It also makes working in teams easier, because each person's changes are stored in a separate version.

More specifically, a VCS allows you to:

* revert files back to a previous state
* review changes made over time
* collaborate on a set of files with others
* see who last modified something that might be causing a problem

Plus it functions as a backup system, a safe place for all your work. Using a VCS means that if you mess things up or lose files, you can generally recover easily. In addition, you get all this for very little overhead.

There are many VCS. Git and GitHub have become the VCS of choice for most software teams. Do you know other VCS?

## Git vs. Github

We'll be using a version control system called **git**. It was created in 2005 to help with developing Linux kernels, and it's now the most popular version control system today.

### Github

Github is not the same as git. **Github** is a social network built around git. It has completely changed the way we, as programmers, share and work on code. GitHub is now the largest online storage space of collaborative works, and it works with git in order to keep track of versions, issues, and requests for changes.

### Github and Git

Together, git on your _local machine_ and git on _Github_ form a **distributed version control system**. In other words, code can be kept track of in different places, allowing multiple people to work on code simultaneously. Let's see how this works.

![DVCS diagram](http://git-scm.com/figures/18333fig0103-tn.png)

In this diagram, we have a project on three different computers, all kept track of under git. Computers A and B are local \(client\) machines that have a copy of the project. The server computer is another machine that allows the clients to pull down any changes that are made to the project.

Throughout WDI, each developer will be pulling down from a server, and that server is **Github!** Once we pull down a copy of the project, we can make changes locally, and eventually push our changes to the server.

## Folder Management

A word about folder management.

Recommendation: Create "Code" folder in your home directory. This is the place for all source code that you create at GA \(projects, labs, assignments\). Let's talk about folder structure.

Options:

* By time
* By topic
* A combination of both

Discuss approach. What works for you? I recommend that you decide on a structure in the first week and stick to it.

