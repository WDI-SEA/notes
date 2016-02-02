#Group Collaboration

##Objectives

* Understand the concepts behind a forking workflow in git
* Setup a repository and have group members utilize the forking workflow
* Identify and assign project roles
* Use a Kanban board to keep track of issues and bugs
* Utilize other tools to communicate effectively
* Review wireframing, user stories, and agile practices

##Git Workflows

So far, we've been using git to save versions of our work, which is one of git's main purposes. The other main purpose has been ignored until now, and that is team collaboration. There are a few different ways to collaborate with a group of people using git/Github.

[Different Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)

We'll be focusing our time on the Forking Workflow. We've actually been using this workflow all along to a lesser degree, when submitting homework.

![Forking](http://i.stack.imgur.com/iYdhN.png)

[Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)

A forking workflow looks something like this. The idea is that...

1. One person acts as the **git master** and creates the main repo. He/she also manages the code that's merged into the repo.
2. Everyone else **forks** the main repo so that they have a copy of it. This copy is **isolated** from the main repo.
3. In the fork, work is done in branches known as **feature branches** until the feature is finished.
4. Once the feature is finished, you'll want to do what's called an **upstream pull.** This will allow any changes from the main repo to be reflect in your fork. Assuming everyone works in separate branches, this should not create any merge conflicts.
5. Once the upstream pull is finished, you can push your changes to the Github fork, and then create a pull request. This will allow the git master to merge the changes.
6. Finally, once the pull requests have finished, pull from the upstream so the latest changes are in the fork.

Let's practice this.

##Forking Workflow Practice

Practice the forking workflow in groups of 3-4.

###Setting up the Repo

* Choose one person to be the **git master**
  * This person should create a new repository. Let's call it `forking-test`
  * Once the repository is created, clone it to your computer
* Once the repo is created by the git master, the other group members should get a link to the new repo and **fork it.**
  * Each group member should clone their forked repo to your computer

###Setting up Upstreams

Try running `git remote -v`. This will be a list of **remote** repositories. By default, `origin` is the remote of your fork on Github. We're going to add another remote to reference the main repo, so if there are any changes, they can be pulled from the main repo into the fork.

* Group members other than the git master should follow these steps
  * Go back to the main repo (not the fork) and copy the SSH link
  * `cd` into your cloned fork
  * Add the remote by running in the terminal (pasting the SSH link in lieu of the one provided):

```
git remote add upstream git@github.com:gitmasterusername/forking-test.git
```

* Testing the upstreams
  * Have the git master create a change in the main repo on the `master` branch. Add the change, commit it, and push it to Github
  * Once the git master has pushed changes, group members should try running `git pull upstream master`

If successful, group members should receive the change in their forks.

###Working on Changes

Practice making changes by creating new branches, switching to them, and making commits. Note that the git master should also be working in a separate branch, as not to pollute the `master` branch. Keep it sacred!

###Merging Changes

Once group members have made some changes in separate branches, push those changes to Github, then try making pull requests on Github.

Once pull requests have been made, the git master should go to Github, view the pull requests, and merge them! Or, you can have a conversation about why the changes shouldn't be merged.

###Conclusion

The forking repo is one of the widely used git workflows available. It's used to contribute to open source projects, as well as internally by some companies.

You may come across problems when working with git, such as merge conflicts and changes not appearing where you think they should be. Keep in mind that while you have the tools available to solve these problems, the biggest challenge is to figure out how!

![XKCD Git](http://imgs.xkcd.com/comics/git.png)

Indeed, git may take a lifetime to "master", but the only true way to master git is to use it. Here are some resources if you need help, or would like to learn about advanced tools beyond branching and rebasing.

* https://www.atlassian.com/git/tutorials
* http://pcottle.github.io/learnGitBranching

##Your Main Project Roles

###Required

####Project Manager (PM)

The project manager, or PM, is responsible for planning and seeing a project from its initiation to its completion. A PM generally has to have strong leadership and communication skills, as well as the ability to keep others motivated and on track. Some other roles may include overseeing the scope of the project, planning out resources, time management, and monitoring progress throughout the project.

####Git Master (Maintainer)

Commonly known as the repository maintainer, but known in WDI as the "git master", the git master's job is to handle incoming pull requests and merge them appropriately. Their job is to handle the **state of the repo** and make sure that everything goes smoothly. Be prepared for merge conflicts if necessary.

###Others you may want to assign

####Front end developer

####Back end developer

####"Full stack" developer

####Database Administrator (DBA)

* Useful if you are working with a complex data schema, with fixtures/seeders to load data

####Other Specialist

* This role will likely be used if you are working with foreign technologies or complex topics, such as D3, front end plugins, machine learning, etc.

##Kanban Boards

![Kanban](https://olemortenamundsen.files.wordpress.com/2010/03/kanban_illustration.png)

**Kanban** literally means billboard in Japanese. For software purposes, it's a board to keep track of logistics and production. It's highly recommended that you make a Kanban board, and luckily, Trello is a great (and free) tool for making them. Recommended sections:

* Backlog (or icebox)
* On deck (next to do)
* Sprint (referring to a software sprint)
* Done

Normally, there would be a section for testing, but since the development cycle in this class is one week, the section will likely be empty most of the time. However, feel free to add it if you'd like.

##Other Handy Tools

* Private Slack channels
* Wireframing (see previous notes)
* User stories (see previous notes)
* Classmates (for testing your app, or creating new users)
* Heroku (for deployment)

##Other Notes

* Communicate FREQUENTLY. You're a team
* Keep wireframes and user stories short and low-fi, in case you need to pivot
* Work on APIs and essential functionality first
  * Working software is the priority
* Know what everyone's working on so that work does not conflict
* Deploy early and often
