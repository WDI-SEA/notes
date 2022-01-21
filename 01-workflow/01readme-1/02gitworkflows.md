# Git Workflows

So far, we've been using git to save versions of our work, which is one of git's main purposes. The other main purpose has been ignored until now, and that is team collaboration. There are a few different ways to collaborate with a group of people using git/Github.

[Different Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)

We'll be focusing our time on the Forking Workflow. We've actually been using this workflow all along to a lesser degree, when submitting assignments.

![Forking](http://i.stack.imgur.com/iYdhN.png)

[Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)

A forking workflow looks something like this. The idea is that...

1. One person acts as the **git manager** and creates the main repo. They also manage the code that's merged into the repo.
2. Everyone else **forks** the main repo so that they have a copy of it.
3. In the forks, work may be done in branches known as **feature branches** until the feature is finished, or you can edit directly in your forked repo. ***It it highly recommended, however, that the git manager always work in feature branches before merging into the main branch.***
4. For the folks working on forks, once a feature is finished, you'll want to do what's called an **upstream pull.** This will allow any changes from the main repo to be reflected in your fork. Assuming everyone works in separate branches, this should not create any merge conflicts.
5. Once the upstream pull is finished, you can push your changes to the Github fork, and then create a pull request. This will allow the git master to merge the changes. ***Make sure to notify them so they can merge your changes right away.***
6. Finally, once a pull request has been merged, **all non-git-managers shoud immediately pull from the upstream so the latest changes are in the fork***. Again, this shouldn't cause any issues if no one deletes or re-arranges files, and if no one works on the same file at the same time.

Let's practice this.

## How to pull (lol) it off

### Setting up the Repo

* Choose one person to be the **git manager**
  * This person should create a new repository. Let's call it `forking-test`
  * Once the repository is created, clone it to your computer
* Once the repo is created by the git master, the other group members should get a link to the new repo and **fork it.**
  * Each group member should clone their forked repo to your computer

### Setting up Upstreams

Try running `git remote -v`. This will be a list of **remote** repositories. By default, `origin` is the remote of your fork on Github. We're going to add another remote to reference the main repo, so if there are any changes, they can be pulled from the main repo into the fork.

* All group members ***except the git manager*** should follow these steps
  * Go back to the main repo \(not the fork\) and copy the HTTP link
  * `cd` into your cloned fork
  * Add the remote by running in the terminal \(pasting the HTTP link in lieu of the one provided\):

```text
git remote add upstream git@github.com:gitmasterusername/forking-test.git
```

* Testing the upstreams
  * **Git Manager:** create a change in the main repo on the `main` branch. Add the change, commit it, and push it to Github.
  * Once the git master has pushed changes, group members should try running `git pull upstream master`

If successful, group members should receive the change in their forks.

### Working on Changes

Practice making changes by creating new branches, switching to them, and making commits. Note that the git master should also be working in a separate branch, as not to pollute the `master` branch. Keep it sacred!

### Sample Practice App

Work in your project groups.

* Git Manager: Create a new react app. The App component should show your team name.
* Non-manager members: 
   * Fork and clone the main repo.
   * Set the upstream to be your Manager's main repo. 
   * Add a component to the /src folder titled with your name. The component should render your name and a photo of you (or a short bio).
   * When you've finished writing your component, commit your changes, push to your fork, and make a pull request.
* Git Manager:
   * Review and merge each pull request.
   * Pull down the newly merged code to your local repo.
   * Edit App.js to render all the new components underneath your team name. Commit and push to the main remote repo.
   * When you're finished merging and editting, notify you're teammates!
* Non-manager members: When your Manager tells you it's ready, pull from the upstream to get the new changes!

### Merging Changes

Once group members have made some changes in separate branches, push those changes to Github, then try making pull requests on Github.

Once pull requests have been made, the git master should go to Github, view the pull requests, and merge them! Or, you can have a conversation about why the changes shouldn't be merged.

### Conclusion

The forking repo is one of the widely used git workflows available. It's used to contribute to open source projects, as well as internally by some companies.

You may come across problems when working with git, such as merge conflicts and changes not appearing where you think they should be. Keep in mind that while you have the tools available to solve these problems, the biggest challenge is to figure out how!

![XKCD Git](http://imgs.xkcd.com/comics/git.png)

Indeed, it may take a whole lifetime to become a git pro, but the only true way to wrangle git flows into your bones is to use it. Here are some resources if you need help, or would like to learn about advanced tools beyond branching and rebasing.

* [https://www.atlassian.com/git/tutorials](https://www.atlassian.com/git/tutorials)
* [http://pcottle.github.io/learnGitBranching](http://pcottle.github.io/learnGitBranching)
