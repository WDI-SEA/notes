# Optional Tools

## iTerm

iTerm is a tricked out version of the Terminal app that is the default command line interface for Mac. It will help with the visuals of the command line navigation, especially with ohmyZSH.

[Download here](https://www.iterm2.com/)

## Node Version Manager

[NVM](https://github.com/nvm-sh/nvm) is a useful tool that allows you to have many versions of node installed and quickly switch bewteen them.

First run this in your terminal:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```

After the install checkout your shell profile in a text editor (`code ~/.zshrc` for zsh or `code ~/.bachrc` for bash) and check to make sure it has the following lines:

```bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

if not, add them.

## Postgres installed by homebrew

Postresql can also be installed by homebrew, and managed similarly to how we have done mongodb.

Run the following commands in your termimal:

```bash
#-------------------------------------------------------------------------------
# Install Postgres
#-------------------------------------------------------------------------------

# install postgresql
brew install postgresql

# fix some issues with older macs
sudo mkdir -p /usr/local/var/postgres/{pg_tblspc,pg_twophase,pg_stat_tmp}

# may also need this on older macs
sudo chmod -R 0700 /usr/local/var/postgres
sudo chown -R ${USER} /usr/local/var/postgres

# launch postgres
brew services start postgres

# create db matching user name so we can log in by just typing psql
createdb ${USER}
```

you can test your installation with the command `psql`, and it should take you to a prompt like this:

```
psql (13.2)
Type "help" for help

[yourusername]=#
```

You now have these commands to manage postgres:

```bash
# start service
brew services start postgres

# stop service
brew services stop postgres

# restart service
brew services restart postgres
```

## python 3 aliases

We a going to alias the `python` command to point to python3 instead of python. We can do this by adding a few lines on code to our zshell config file.

___

Run the command `code ~/.zshrc` from anywhere in your terminal to open up the zshell config file (it lives in your home directory and this an an exact path command).

Scroll down to the command aliases area of the file (you can find the different areas by reading the comments) and paste the following lines of shell script in:

```bash
# python3 aliases
alias python=python3
alias pip=pip3
```

Afterwards, save the file and close vscode. Restart your terminal and use the command `python --version` and it should return `Python 3.9.2`.

If it still says `Python 2.blah.blah` you probably forgot to restart your terminal.

## All Systems

Everyone needs to install the following things, regardless of thier operating system.

1. install a couple global python packages with `pip3`
1. install a vscode extension for python

### Other Code Editor Options

We will use VS Code in this class, but if you're more familiar with another editor or would like to try out another editor, check these out:

**Sublime Text 3**

A very popular shareware code editor with a vast library of extensions. It will nag you to purchase it every fourth time you save a file.

Download and install version 3 from [http://www.sublimetext.com/3](http://www.sublimetext.com/3)

It is a pretty typical installation for an app, but we need to add a shortcut so we can load sublime from the Terminal.

```text
ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
```

Restart terminal, and you should be able to open a folder to edit by typing `subl .`

**Atom**

Atom boasts tighter integration with Git and Github as well as being open source \(which means no purchase nags.\)

Download and install Atom from [here](https://atom.io/)

For a command line shortcut, run this:

```text
ln -s /Applications/Atom.app/Contents/Resources/app/atom.sh /usr/local/bin/atom
```

Now you can open a folder from your terminal by typing: `atom .`

#### Add quick `.zshrc` access

In your `~/.zshrc`, add these two functions and environment variables to make it easier to access, change and refresh our ZSH configuration file in the future. Copy and paste these to the end of the file.

```text
export VISUAL=code
export EDITOR="$VISUAL"

function zedit() {
  code ~/.zshrc
}

function zrefresh() {
  echo "Refreshing your ZSH configuration."
  source ~/.zshrc
}
```

If you plan on using Sublime Text, replace `code` with `subl`. If you plan on using Atom, replace`code` with `atom`.

Save the file and restart your terminal.

#### Install Postgres GUI

Mac users can utilize **Postico**. Install here:

[https://eggerapps.at/postico/](https://eggerapps.at/postico/)

#### Change where your `mongodb` data is stored

```text
#make data directory
sudo mkdir -p ~/mongodb-data
```

After creating the data directory in your home folder, it should be marked with your correct ownership permissions but if you find that it is owned by root instead, you can change it to be owned by you with the following commands:

```bash
#get your user name
whoami

#set data directory permissions (replacing USERNAME with the result from whoami above)
sudo chown -R USERNAME:wheel ~/mongodb-data
```

Finally, to tell MongoDB to start using the data directory that you just created, you must start it with the following command:

```bash
mongod --dbpath ~/mongodb-data
```

To make a shortcut for this command, open your ~/.zshrc \(or ~/.bashrc if not using ZSH\) and add this line to the bottom:

```bash
alias mongod="mongod --dbpath ~/mongodb-data"
```

**Install MongoDB GUI**

One of the most common free MongoDB GUIs is **RoboMongo**. Install here:

[https://robomongo.org/](https://robomongo.org/)
