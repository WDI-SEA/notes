# WSL Installfest

## VS Code

Install VS Code for Windows from [this link](https://code.visualstudio.com/download).

Once VS Code is installed, open it and go to the 'Extensions' tab and install the '`Remote - WSL`' extension.

You should be able to now open your WSL terminal \(the Ubuntu app\) and execute the `code` command, which will automatically open VS Code for you if it isn't already open

## Git

You should already have an account on GitHub from Fundamentals. If not, sign up for an account on [github.com](http://github.com). We'll be using GitHub to track code changes and collaborate on projects.

First off, you will need to add the git-core PPA \(Personal Package Archive\) to get the most recent version of Git.

Run these three commands one by one in your WSL terminal:

```text
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

1. Use the following three `git config` commands to configure your git user information and have git "cache" \(remember\) it. We use the `--global` \(or `-g`\) option to make the configuration apply to all repositories.

![git config](../../../.gitbook/assets/gitconfig.png)

To view your git configurations, you can either run following commands on the terminal

```text
git config --list
```

OR

```text
git config user.name
git config user.email
```

### Check your Git version

Now let's check the version of Git we have installed. We want to have version 2.28 or above.

To view your Git version, run the following command on the terminal

```text
git --version
```

If your git version comes back as 2.28 or above, then we are good to continue to the next config step - which is to change the default branch name to `main`

```text
git config --global init.defaultBranch main
```

Follow the instructions [here](https://gasei.gitbook.io/sei/00-config-deployment/installfest/osx/unit-1#optional-setting-up-an-ssh-key-for-github) to set up an SSH key for github. Add the SSH key to your [open source github](https://github.com/). 

other git config settings that are optional, but reccomend:

```bash
# rebase by default on pull
git config pull.rebase true
# optional: set the default git editor to be vscode to aviod getting stuck in vim
git config --global core.editor 'code -w'
git config --global push.default simple
```

### Zsh Install

Open the Ubuntu terminal app In the terminal run the following commands: \(follow the prompts and press y to confirm yes when it prompts you to\)

```text
sudo apt install zsh
chsh -s $(which zsh)
```

Exit the ubuntu terminal and reopen it. It will prompt you with the Z Shell configuration menu - press 2 to populate zsh with the recommended defaults



## Navigation

1. Read this intro
   * \[✔️\] [Alternative OS intro](./)  
2. Prior to the first day of class: Enable WSL and Install Ubuntu from the Microsoft Store app
   * \[✔️\] [WSL Setup](wsl-setup.md)
3. On the first day of class, your instructors will help you with **Installfest**
   * \[✔️\] [Installfest](wsl-installfest.md)
4. Optional visual and usability upgrades for your terminal
   * [ ] [Visual Upgrades](upgrades.md)
5. Unit 2-4 Installfest
   * [ ] [Unit 2, 3, 4 Installfest](wsl-unit234.md)

