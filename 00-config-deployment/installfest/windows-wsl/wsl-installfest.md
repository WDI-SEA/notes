# Installfest

## VS Code
Install VS Code for Windows from [this link](https://code.visualstudio.com/download).

Once VS Code is installed, open it and go to the 'Extensions' tab and install the '`Remote - WSL`' extension.

You should be able to now open your WSL terminal (the Ubuntu app) and execute the `code` command, which will automatically open VS Code for you if it isn't already open


<br />

## Git

You should already have an account on GitHub from Fundamentals. If not, sign up for an account on [github.com](http://github.com). We'll be using GitHub to track code changes and collaborate on projects.

First off, you will need to add the git-core PPA (Personal Package Archive) to get the most recent version of Git.

Run these three commands one by one in your WSL terminal:

```
# Add the repo with the most up-to-date version of git
sudo add-apt-repository ppa:git-core/ppa

# Update and upgrade your programs
sudo apt-get update
sudo apt-get upgrade
```

### Confirm Install

1. To check whether git is installed on your system, run the Terminal command `which git`. The output should be a directory path like `/usr/bin/git`. This is where git is installed on your machine. If you don't see any output, git is not installed on your computer.

### Configure Git

Configuring your git settings will help GitHub track your contributions and to make it easier and smoother to commit changes.

1. Use the following three `git config` commands to configure your git user information and have git "cache" (remember) it. We use the `--global` (or `-g`) option to make the configuration apply to all repositories.

<p align="center">
<img src='./gitconfig.png' width='600px' alt='git config'>
</p>

To view your git configurations, you can either run following commands on the terminal

```
git config --list
```
OR

```
git config user.name
git config user.email
```
### Check your Git version

Now let's check the version of Git we have installed. We want to have version 2.28 or above.

To view your Git version, run the following command on the terminal

```
git --version
```

If your git version comes back as 2.28 or above, then we are good to continue to the next config step - which is to change the default branch name to `main`

```
git config --global init.defaultBranch main
```

<br />

## Node.js

We're going to install Node.js using a tool called Node Version Manager (NVM for short). Node has been around for a while and has many versions available for us to use. We're going to focus on the latest Longterm Support (LTS) version for our work in the course.

1. Run the following command to download and run the `nvm` install script via `curl`:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```

* ***Important Note***! If you've installed or plan to install Zsh and use that instead of bash, you will need to run the following command instead:
```bash
# Run this command instead if you're using Zsh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | zsh
``` 

2. Double check that NVM installed correctly with:

```bash
nvm --version
```

3. Finally we're ready to install Node. We want the latest LTS version. To get it and use it, run these commands:

```bash
nvm install --lts
```

> Your console should display a progress bar during installation. Wait for this to complete before continuing.

4. Use the lts version of node.

```bash
nvm use --lts
```

5. Set the default Node version.
```bash
nvm alias default node
```

<hr />

## Navigation
1. Read this intro
    * [✔️] [Alternative OS intro](./README.md)  
2. Prior to the first day of class: Enable WSL and Install Ubuntu from the Microsoft Store app
    * [✔️] [WSL Setup](./wsl-setup.md)
3. On the first day of class, your instructors will help you with **Installfest**
    * [✔️] [Installfest](./wsl-installfest.md)
4. Optional visual and usability upgrades for your terminal
    * [ ] [Visual Upgrades](./upgrades.md)
5. Unit 2-4 Installfest
    * [ ] [Unit 2, 3, 4 Installfest](./wsl-unit234.md)