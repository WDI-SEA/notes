# Hosting on Github Pages

## Objectives
* Understand some of the benefits of hosting on [Github Pages](https://pages.github.com/)
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

### Setup Your Main Page

Enable GitHub Pages in your GitHub account by creating a new specially-named repo named `username.github.io`. This repo contains HTML, JS and CSS that acts as your GitHub Pages homepage. Once you have this main repo set up you can make other repos available too.

Follow instructions on [Github Pages](https://pages.github.com/) to initialize GitHub Pages in your GitHub account.

1. [Create a new repository](https://github.com/new) named `username.github.io` where `username` is your GitHub username.
2. Clone the new repo to your computer `git clone https://github.com/username/username.github.io`
3. Change your directory to the repo `cd username.github.io`
4. Create a simple Hello World homepage: `echo "Hello World" > index.html`
5. Add new files, commit the change, and push the repo.

```
git add -A
git commit -m "Initial commit"
git push -u origin master
```

6. View the now-hosted page! http://username.github.io.

### Add Another Repo to GitHub Pages

Github Pages works by serving HTML/CSS/JavaScript files that live in a separate branch.

Think of a branch as a separate "timeline" for your code. It can represent a set of different commits. We've been dealing with the **master** branch so far, but now we'll introduce a new branch for deployment called **gh-pages**

1. Choose an existing repo that you want to host on GitHub Pages.
2. Checkout that repo on your local machine.
3. Make sure you're on the master branch: `git checkout master`
3. Create the special gh-pages branch: `git checkout -b gh-pages`

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

