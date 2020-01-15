# SEI Seattle Install Fest

For the first portion of the class, we'll be working exclusively inside of the browser and Node. We'll be installing the following tools.

* Slack
* Homebrew
* Git
* Node
* Oh my ZSH
* iTerm
* Postgres.app
* Ruby
* Rails

## Slack

We will be using slack to communicate throughout the course. You should've received an invite to our channels via e-mail. You can login via the web browser, but downloading / installing the app is highly recommended.

[Download Slack](https://slack.com/downloads)

## Homebrew

Homebrew is a package manager that we will use to install various command line tools in our class.

Open up terminal, and paste the following command to install Homebrew. You might be prompted to install XCode Command Line Tools during the install process.

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

You may be prompted to installed XCode command line tools. When prompted, click and install through that, and you're homebrew installation will continue.

After the installation process, run the command `brew doctor`. If any warnings or errors are displayed, we will need to resolve them before proceeding with the rest of the install fest.

## Xcode

We do not use Xcode in class but some other applications that we do use require some Xcode libraries. Normally, all you need is the Xcode CLI which should have already been installed when you installed Homebrew. If it didn't get installed, you can use this command:

```
xcode-select --install
```

If you need to, you can install Xcode through the App Store. [Link here](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)

## GIT
Before we do this process, please make sure you have signed up for an account on [Github](http://www.github.com). We will be installing a version of GIT from home brew and also configuring it.

To install GIT
```
brew install git
```

#### Configuring GIT

Using your email credentials for GIT, run these commands with your user and email configured.

```
git config --global user.name "YOUR-USERNAME"
git config --global user.email "YOUR-EMAIL-ADDRESS"
git config --global push.default simple
git config --global credential.helper cache
```

#### Setting up SSH Key

You might find your self having to re-authenticate GIT every time you work on your command line. Setup SSH Keys to let Github remember your machine in the future.

* [Github Generating SSH Keys](https://help.github.com/articles/generating-ssh-keys/)

## Node

To install Node
```
brew install node
```

Verify the installation afterwards by running

```
node -v
npm -v
```

The above should display without any errors.

To finish up your installation, run this command to allow for global installations of npm tools.

```
sudo chown -R $USER /usr/local/lib
```

## Install Oh My ZSH

Oh my ZSH?!!! We will be tricking out commandline with another shell. A shell is an interface into our computer, and we will be using a lot to run commands.

We'll be using a shell and configuration package called [Oh-My-Zsh](https://github.com/robbyrussell/oh-my-zsh)

To install, we will run

```
curl -L http://install.ohmyz.sh | sh
```

Restart Terminal, and you should see a brand new and colorful command prompt.

# Code Editor Options

### VS Code

Currently the most popular editor according to developer polls. This is Microsoft's free version of Visual Studio.

Download and install VS Code from [here](https://code.visualstudio.com/download)

To be able to open VS Code from any directory, add it to your path inside your ~/.zshrc file:

```bash
export PATH=$PATH:"/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```

Save this file and then fully restart your terminal window (quit and restart.)


### Sublime Text 3

A very popular shareware code editor with a vast library of extensions. It will nag you to purchase it every fourth time you save a file.

Download and install version 3 from [http://www.sublimetext.com/3](http://www.sublimetext.com/3)

It is a pretty typical installation for an app, but we need to add a shortcut so we can load sublime from the Terminal.

```
ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
```

Restart terminal, and you should be able to open a folder to edit by typing `subl .`

### Atom

Atom boasts tighter integration with Git and Github as well as being open source (which means no purchase nags.)

Download and install Atom from [here](https://atom.io/)

For a command line shortcut, run this:

```
ln -s /Applications/Atom.app/Contents/Resources/app/atom.sh /usr/local/bin/atom
```

Now you can open a folder from your terminal by typing: `atom .`

## Postgres

### Postgres.app
We will be using a relational database called Postgres during our class.

Download and install from [http://postgresapp.com/](http://postgresapp.com/)

If you have successfully configured zsh and sublime or atom, the following command should work.

```
subl ~/.zshrc
```

-OR-

```
atom ~/.zshrc
```

Your sublime (or Atom) editor will popup with configuration settings, at the bottom of the file append

```
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.6/bin
```

While we're here, add these two functions and environment variables to make it easier to access, change and refresh our ZSH configuration file in the future. Copy and paste these to the end of the file.

If you plan on using Sublime Text copy this:

```
export VISUAL=subl
export EDITOR="$VISUAL"

function zedit() {
  subl ~/.zshrc
}

function zrefresh() {
  echo "Refreshing your ZSH configuration."
  source ~/.zshrc
}
```

Otherwise, if you plan on using Atom, copy this instead:

```
export VISUAL=atom
export EDITOR="$VISUAL"

function zedit() {
  atom ~/.zshrc
}

function zrefresh() {
  echo "Refreshing your ZSH configuration."
  source ~/.zshrc
}
```

Save the file, close Sublime (or Atom), and restart your terminal.

Type `which psql` at which point should display

```
/Applications/Postgres.app/Contents/Versions/9.5/bin/psql
```

### Install Postgres GUI

We'll be using **Postico**. Install here:

https://eggerapps.at/postico/

## Installing MongoDB (Updated 11/2019)

**Notes:** The name of the free version of MongoDB has changed to `mongodb-community` as of November 2019. Also, the Catalina version of MacOS (version 10.15) disallows folders being created at the root of the file system so you must create your MongoDB data folder inside your home folder

```sh
#Install MongoDB
brew install mongodb-community

#make data directory
sudo mkdir -p ~/mongodb-data
```

After creating the data directory in your home folder, it should be marked with your correct ownership permissions but if you find that it is owned by root instead, you can change it to be owned by you with the following commands:

```sh
#get your user name
whoami

#set data directory permissions (replacing USERNAME with the result from whoami above)
sudo chown -R USERNAME:wheel ~/mongodb-data
```

Finally, to tell MongoDB to start using the data directory that you just created, you must start it with the following command:

```sh
mongod --dbpath ~/mongodb-data
```

To make a shortcut for this command, open your ~/.zshrc (or ~/.bashrc if not using ZSH) and add this line to the bottom:

```sh
alias mongod="mongod --dbpath ~/mongodb-data"
```

### Testing the MongoDB server

```
#Start the MongoDB server
mongod
```

Press `control-c` to stop the server.

### Install MongoDB GUI

We'll be using **RoboMongo**. Install here:

https://robomongo.org/

## Installing Python 3

Brew is also used to install Python 3. (Python 2 is already installed on your Mac.) To install Python 3 without errors, we first need to create a couple directories and change them to be owned by us:

```
mkdir /usr/local/lib
mkdir /usr/local/Frameworks
whoami
```
Make a note of the username returned from `whoami`. Enter that username in place of USERNAME below:
```
sudo chown -R USERNAME:wheel /usr/local/lib
sudo chown -R USERNAME:wheel /usr/local/Frameworks
```

If you received no errors from those commands, then use this command to install version 3:

```
brew install python3
```

You can test the installation by running `python3 --version`.

This should also install `pip3`, a package installer for Python 3. You can verify that it is installed and working by updating it with the following command:

```
pip3 install --upgrade pip setuptools wheel
```

This should return some normal messages - no errors. Now that `pip3` is working, we can use it to install a useful Python shell:

```
pip3 install ipython
```

iPython makes it easy to write python code in your terminal. We may not use it a huge amount but it is handy to have around.


# Archive Resources from Previous Curriculum

## Installing Django

We will also use `pip3` to install Django, a robust back-end server for Python. We will be installing the 2.0.x version:

```
pip3 install Django
```

## Installing Ruby on Rails

### Install rbenv
rbenv lets us change ruby verions on the fly, useful for working with diffrent versions.

```
brew update
brew install rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(rbenv init -)"' >> ~/.zshrc
source ~/.zshrc

sudo chown -R $USER ~/.rbenv
```

### Configuring rbenv
__Note: new versions of Ruby and Rails are released regularly. Check with your instructor whether the versions listed below is appropriate__

```
brew update

brew install ruby-build

rbenv install 2.4.1
rbenv global 2.4.1
```

### Install Rails

```
echo "gem: --no-ri --no-rdoc" > ~/.gemrc
```

Restart your terminal. The command above will install gems without documentation (which can take up time when installing Rails)

```
sudo gem update
sudo gem install rails
```
You may need to press "yes" for various entries

## Verify your installation

Make sure to restart your terminal and then run each of these commands. Finally call someone over to validate your installation is correct.

```
rails -v
ruby -v

which ruby
which rails
which bundle
which gem

node -v
npm -v

git --version
psql --version
subl -v (or atom -v)

```

### Overwriting an existing Ruby installation

You may already have an old version of Ruby installed. In this case, it may be easiest to update your Ruby version with [RVM - Ruby Version Manager](https://rvm.io/rvm/install#basic-install). The stable option will install RVM with the latest stable (tested and approved) version of Ruby.

```
\curl -sSL https://get.rvm.io | bash -s stable --ruby
```

### RVM Cheat Sheet
Now that you have RVM, some useful commands it can perform:

```
rvm list known
```

This lists all known versions of Ruby 

```
rvm install X.X
```

Install version X.X of Ruby (where you replace the X's with the appropriate version number you would like to install).

```
rvm use X.X
```

If you have multiple versions of Ruby, you must tell your computer which one to use as the primary or default version.

```
rvm use X.X --default
```

This does the same as the above command, but additionally sets this version of Ruby as the default for any new shells you might use.

Refer to [RVM documentation](https://rvm.io/) for any further RVM questions.
