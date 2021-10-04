# Linux

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

**TIP:** Use `CTRL+SHIFT+V` to paste into terminal

## Slack

We will be using slack to communicate throughout the course. You should've received an invite to our channels via e-mail. You can login via the web browser, but downloading / installing the app is highly recommended.

[Download Slack](https://slack.com/downloads)

## GArnet

~~We will be using GArnet to manage the course. You'll be able to see a list of assigned deliverables, submissions, evaluations, and your attendance record. Your managers will give you an invite link.~~

GA Seattle isn't currently using this system - your homework progress and attendance will be reported to you regularly by your instructor and is also available on request.

## GIT

Before we do this process, please make sure you have signed up for an account on [Github](http://www.github.com). We will be installing a version of GIT from home brew and also configuring it.

To install GIT

```text
sudo apt-get install git-all
```

#### Configuring GIT

Using your email credentials for GIT, run these commands with your user and email configured.

```text
git config --global user.name "YOUR-USERNAME"
git config --global user.email "YOUR-EMAIL-ADDRESS"
git config --global push.default simple
git config --global credential.helper cache
```

#### Setting up SSH Key

You might find your self having to re-authenticate GIT every time you work on your command line. Setup SSH Keys to let Github remember your machine in the future.

* [Github Generating SSH Keys](https://help.github.com/articles/generating-ssh-keys/)

## Node

```text
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

sudo apt-get install -y build-essential nodejs
```

Verify the installation afterwards by running

```text
node -v
npm -v
```

The above should display without any errors.

To finish up your installation, run this command to allow for global installations of npm tools.

```text
sudo chown -R $USER /usr/local/lib
```

## Sublime 3

We'll be running **Sublime 3**, not Sublime 2 as our text editor of choice.

Install via the package manager

```text
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer
```

If the above does not work, try installing via Sublime's website: [http://www.sublimetext.com/3](http://www.sublimetext.com/3) Download the `.deb` file and run it to install.

## Install Oh My ZSH

Oh my ZSH?!!! We will be tricking out commandline with another shell. A shell is an interface into our computer, and we will be using a lot to run commands.

We'll be using a shell and configuration package called [Oh-My-Zsh](https://github.com/robbyrussell/oh-my-zsh)

To install, we will run

```text
sudo apt-get update
sudo apt-get install git-core zsh
chsh -s /bin/zsh
wget --no-check-certificate http://install.ohmyz.sh -O - | sh
sudo shutdown -r 0
```

\(the last command will restart your computer\)

## Postgres

### Install Postgres

We will be using a relational database called Postgres for Node and Rails portion our class. Download by running:

```text
sudo apt-get install postgresql-client postgresql postgresql-contrib
```

### Configure Postgres User

You'll also need to configure a user for your Postgres database.

```text
sudo -u postgres psql postgres

\password postgres
```

Choose an easy to remember password then type `\quit` to exit psql. MAKE SURE YOU REMEMBER THIS PASSWORD YOU WILL NEED IT LATER.

### Create a Postgres Alias

To make it easier to start postgres we're going to create a couple aliases. Edit your zshrc file by typing `subl ~/.zshrc` add these lines to the bottom of the file:

```text
alias psql="sudo -u postgres psql"
alias pgserver="sudo -u postgres service postgresql start"
```

**pgserver** will be used to start the postgres server

**psql** will be used to access the psql termainal

While we're here, add these two functions and environment variables to make it easier to access, change and refresh our ZSH configuration file in the future. Copy and paste these to the end of the file.

```text
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

Save the file, close Sublime, and restart your terminal.

### Install Postgres GUI

```text
sudo apt-get install pgadmin3
```

### Testing Postgres Setup

Quit terminal and reopen it before testing.

**Start Server**

```text
pgserver
```

**enter psql terminal**

```text
psql
```

Should enter psql terminal and have no error.

**exit psql**

```text
\q
```

## Installing MongoDB

Follow the official installation instructions on MongoDB.com:

[https://docs.mongodb.com/v3.0/tutorial/install-mongodb-on-ubuntu/\#install-mongodb](https://docs.mongodb.com/v3.0/tutorial/install-mongodb-on-ubuntu/#install-mongodb)

### Testing the MongoDB server

```text
#Start the MongoDB server
mongod
```

Press `control-c` to stop the server.

### Install MongoDB GUI

We'll be using **RoboMongo**. Install here:

[https://robomongo.org/](https://robomongo.org/)

## Installing Ruby on Rails

#### Install dependencies

```text
sudo apt-get update
sudo apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev
```

### Install rbenv / ruby

rbenv lets us change ruby verions on the fly, useful for working with diffrent rails apps.

**Note: New versions of Ruby and Rails are coming out all the time - check with your instructor that the version listed here is still correct. If you need to install multiple versions of Ruby, it may be easier to use the** [**RVM - Ruby Version Manager**](https://rvm.io/rvm/install#basic-install) **which is described in detail under the osx section of this install instructions.**

```text
cd ~
git clone git://github.com/sstephenson/rbenv.git .rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(rbenv init -)"' >> ~/.zshrc
exec $SHELL

git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.zshrc
exec $SHELL

sudo chown -R $USER ~/.rbenv

rbenv install 2.4.0
```

\(last step above will take a LONG time\)

**Set ruby version and check that it worked**

```text
rbenv global 2.4.0
ruby -v
```

#### Install Rails

Before moving on close and reopen terminal.

```text
gem update
echo "gem: --no-ri --no-rdoc" > ~/.gemrc
gem install bundler
gem install rails
```

\(the last step will take a while\)

## Verify your installation

Run each of these commands and then call someone over to validate your installation is correct.

```text
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
subl -v
```

