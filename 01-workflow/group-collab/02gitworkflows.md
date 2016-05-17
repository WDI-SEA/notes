#Git Workflows

So far, we've been using git to save versions of our work, which is one of git's main purposes. The other main purpose has been ignored until now, and that is team collaboration. There are a few different ways to collaborate with a group of people using git/Github.

[Different Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)

We'll be focusing our time on the Forking Workflow. We've actually been using this workflow all along to a lesser degree, when submitting assignments.

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

### Sample Practice App

Work in your project groups to create a group home page. The homepage should have a main page
showing a picture for each person in the team with their name. Additionally, the practice app
should have a page for each person on the team. Clicking on someone's name or picture should
lead to a page with a short bio for the team member.

Work as a team to decide how the project will be set up. Will you create a simple static HTML page,
or will you create a node app, or will you use Ruby on Rails? Everyone will work on their own
bio pages individually. Each team member should add their own link to their bio page on the home
page. Practice branching, merging and resolving merge conflicts.

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
