![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

# Hosting on Github Pages

## Objectives
* Understand some of the benefits of hosting on Github Pages
* Create a Github page using the automatic generator
* Create a Github page manually (using your own HTML/CSS/JS)

## Deploying your web application using Github Pages

### Why?

* It's free
* It's a quick and easy deployment option for front-end applications with no server-side code.
* Links you to a community of other developers through Github

### Pages gone Viral
* Probably the most well-known front-end app hosted on Github Pages: [2048](http://gabrielecirulli.github.io/2048/)
* Read more about [the game and the Italian developer, Gabriele Cirulli](https://en.wikipedia.org/wiki/2048_(video_game))
* If you're ever bored and want to [make your own 2048](http://2048.directory/), you can fork Gabriele's game.

### Setup

Make sure that you have a separate Github repository for your project.

### `gh-pages` branch

Github Pages works by serving HTML/CSS/JavaScript files that live in a separate branch.

Think of a branch as a separate "timeline" for your code. It can represent a set of different commits. We've been dealing with the **master** branch so far, but now we'll introduce a new branch for deployment called **gh-pages**

### Creates the gh-pages branch

From your project repository, make sure you're on the master branch, and then create the gh-pages branch:

```
git checkout master
git checkout -b gh-pages
```

This creates and switches you to the `gh-pages` branch.

Add the files you want to deploy, if necessary:

```
git add index.html
git add css/*
git add js/*
...
```

Then, commit and push the local `gh-pages` branch up to Github:

```
git commit -m "Deploying the first version of my project"
git push -u origin gh-pages
```

Now go to your page at `http://[your Github user name].github.io/[repo name]`

### Deploying subsequent changes to Github Pages

When working on your project, your changes are committed to the `master` branch. But your public site lives on a separate branch, `gh-pages`. So if you want changes to be displayed live, you'll have to merge the changes made in `master` to `gh-pages`.

Let's say I made two commits on `master` and I'm ready to deploy those changes. First, checkout the `gh-pages` branch.

```
git checkout gh-pages
```

Then merge the changes from `master`.

```
git merge master
```

Once you run the `merge` command, vim (a text editor) may pop up. Just type `:q` and then `ENTER`.

Awesome, now push your local changes up to Github by running `git push`

