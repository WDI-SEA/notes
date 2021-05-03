# (W)installfest
This guide will help you set up your development environment on Windows using **WSL**!

WSL is a tool that allows us to run a linux distribution seamlessly inside of Windows. With WSL, we can develop using linux programs and shell commands.


## The tools we'll be installing
* **W**indows **S**ubsystem for **L**inux 2 (WSL 2)
* VS Code 
* Git
* Zsh
* Oh My Zsh
* Powerlevel10k
* Windows Terminal
* Node.js 
* PostgresQL
* MongoDB

# WSL
First, read [Microsoft's WSL introduction](https://docs.microsoft.com/en-us/learn/modules/get-started-with-windows-subsystem-for-linux/1-introduction).

## Install WSL & Update to WSL 2
* [Enable WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-1---enable-the-windows-subsystem-for-linux) and install a linux distribution ([Ubuntu](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab) is recommended)
    * **IMPORTANT**: be sure to remember the user name and password you use when installing linux, you will be using them a lot! Choose something easy to type and remember.

* Follow the above guide on steps 1-6. After that run the ["Set your distribution version to WSL 1 or WSL 2"](https://docs.microsoft.com/en-us/windows/wsl/install-win10#set-your-distribution-version-to-wsl-1-or-wsl-2) steps as follows:
    * In `Powershell` (ran as administrator):
```shell 
wsl --list --verbose
wsl --set-version Ubuntu 2
wsl --set-default-version 2
```
* [Configuration instructions](https://defragged.org/2020/10/29/how-to-copy-paste-in-windows-subsystem-for-linux-wsl/) to allow Copy + Paste via Ctrl + Shift + C/V

Congrats! We now have Ubuntu installed via WSL!

![ubuntu](https://i.imgur.com/rZZQKlQ.png)

# VS Code
VS Code is the code editor we'll be using throughout the course.
* Download [VS Code](https://code.visualstudio.com/) from their website
* Install the `Remote - WSL` extension in the extensions tab

# Git
Git is the program we use to save and version control our code.

We want to install at least version 2.28, so we'll be installing via [ppa](https://itsfoss.com/ppa-guide/)

Run these three commands one by one in your WSL terminal:
```
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt upgrade
```
## Configuring GIT Locally

Before we do this process, please make sure you have signed up for an account on Github and have your user name and account email ready

Using your github username and email, run these commands one by one replacing “YOUR-USERNAME” and “YOUR-EMAIL-ADDRESS” with the credentials you used to sign up for github.

```
git config --global init.defaultBranch main
git config --global user.name "YOUR-USERNAME"
git config --global user.email "YOUR-EMAIL-ADDRESS"
git config --global push.default simple
git config --global credential.helper cache
```

## Setting up SSH Key to connect to github

In this next part we will generate a SSH key on our local machine, and then link it to our github account. 

There are a few steps to the process, and we are going to follow github’s guide found here:

[Github Generating SSH Keys](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

## Starting the ssh-agent
To prevent your computer from demanding login credentials every time you want to push to github from your local machine - perform the following steps from this [article](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)

```
eval `ssh-agent -s`
ssh-add ~/.ssh/id_ed25519
```

# Zsh, OhMyZsh, and P10k Theme + Font
We'll be using `Zsh` as our shell, rather than the default linux shell `bash`. 

A shell is a text based **C**ommand **L**ine **I**nterface (CLI) with which we can interact with our computer to run programs and commands.

There are a number of advantages to using Zsh, primarily in the customizability and aesthetics department!

## Zsh install
* Open the `Ubuntu` terminal app
* In the terminal run the following commands: (follow the prompts and press `y` to confirm yes when it prompts you to)
```
sudo apt install zsh
chsh -s $(which zsh)
```
* Exit the ubuntu terminal and reopen it. It will prompt you with the Z Shell configuration menu - press `2` to populate zsh with the recommended defaults

## Oh My Zsh install
You will notice that your terminal looks ugly as sin - lets fix that with Oh My Zsh
* [Install instructions](https://ohmyz.sh/#install)
* Run the following command in the `Ubuntu` terminal
```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## Powerlevel10k install
You will notice that there are some broken text icons - that's because the default windows fonts don't support icons.

Let's fix that with Powerlevel10k
* [Instructions](https://github.com/romkatv/powerlevel10k#oh-my-zsh)
```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```
* Edit the `.zshrc` config file with our newly downloaded theme
```
code ~/.zshrc
```
* Find the `ZSH_THEME` line and set it to be
```
ZSH_THEME="powerlevel10k/powerlevel10k"
```

## Font Install
* [Instructions as well as various font suggestions can be found here](https://github.com/romkatv/powerlevel10k#manual-font-installation)

* Download and install the following font files
    - [MesloLGS NF Regular.ttf](
    https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf)
    - [MesloLGS NF Bold.ttf](
    https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf)
    - [MesloLGS NF Italic.ttf](
    https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf)
    - [MesloLGS NF Bold Italic.ttf](
    https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf)
* Right click the Ubuntu terminal header bar, click on 'Properties', click on the 'Font' tab, and change the font fo 'MesloLGS NF', or whichever other font you've installed!


The next time you open your terminal - it'll prompt you to run the powerlevel10k config tool. You can also manually run the tool with:
```
p10k configure
```
Now you can customize your terminal however you wish!


# Windows Terminal (Optional)
Windows terminal is an application that gives you more flexibility and customizability with your terminal window than the regular terminal. 

Nice features include tabs and color themes

* Install from the [Windows Store](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?rtc=1#activetab=pivot:overviewtab)
* Go to Settings -> Profiles -> Ubuntu -> Click on 'Open JSON file' in the bottom left
* Open the JSON file with VS Code or notepad
* Under "profiles" -> "list" find the one with `"name": "Ubuntu",` and add:
```
"commandline": "wsl.exe ~",
"fontFace": "MesloLGS NF",
```


# Node.js
To install Node, we'll first be installing Node Version Manager (nvm)
* [Installation instructions](https://github.com/nvm-sh/nvm#install--update-script)
* Run the following command in your terminal:
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | zsh
```
* Check that `nvm` installed correctly:
```
command -v nvm
```
* Install the latest version of node:
```
nvm install node
```



# 🛑 Unit 2 - PostgresQL
**Stop!** The following instructions pertain to unit 2 - revisit this section in unit 2!

When it comes to installing database technologies - WSL has a handful of extra configuration steps as the installations will not work by default.

### [Install Instructions](https://www.postgresql.org/download/linux/ubuntu/)
```
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql
```

### WSL-specific configuration instructions
By default on WSL - running the `psql` command will give you an error similar to:

`psql: error: FATAL: role "<your_username>" does not exist`

## The fix:
* Run the following commands one by one, but change `<your_user_name>` to your linux username!
```
# Auto start the postgres server
sudo -u postgres pg_ctlcluster 13 main start

# Create a postgres user that matches your username
sudo -u postgres createuser <your_user_name>

# Create a postgres database that matches your username
sudo -u postgres createdb <your_user_name>

# Run psql as the postgres user
sudo -u postgres psql
```

* The last command will bring you inside of the `psql` shell - run the following command
```
ALTER USER <your_user_name> WITH SUPERUSER;
```


# 🛑 Unit 3 - MongoDB
**Stop!** The following instructions pertain to unit 3 - revisit this section in unit 3!

When it comes to installing database technologies - WSL has a handful of extra configuration steps as the installations will not work by default.

* Run the following commands one by one:
```
sudo apt install mongodb
sudo service mongodb start
```

* Test if it worked by running the `mongo` command. If you are in the mongo shell, then it worked!
* If it didn't work, and you get an error referring to `/data/db ` - run the following:
```
sudo mkdir -p /data/db
sudo chmod 777 /data/db
mongod --dbpath /data/db
```