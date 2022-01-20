# Archived Resources from Previous Curriculum

## Installing Django

We will also use `pip3` to install Django, a robust back-end server for Python. We will be installing the 2.0.x version:

```text
pip3 install Django
```

## Installing Ruby on Rails

### Install rbenv

rbenv lets us change ruby verions on the fly, useful for working with diffrent versions.

```text
brew update
brew install rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(rbenv init -)"' >> ~/.zshrc
source ~/.zshrc

sudo chown -R $USER ~/.rbenv
```

### Configuring rbenv

**Note: new versions of Ruby and Rails are released regularly. Check with your instructor whether the versions listed below is appropriate**

```text
brew update

brew install ruby-build

rbenv install 2.4.1
rbenv global 2.4.1
```

### Install Rails

```text
echo "gem: --no-ri --no-rdoc" > ~/.gemrc
```

Restart your terminal. The command above will install gems without documentation \(which can take up time when installing Rails\)

```text
sudo gem update
sudo gem install rails
```

You may need to press "yes" for various entries

## Verify your installation

Make sure to restart your terminal and then run each of these commands. Finally call someone over to validate your installation is correct.

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
subl -v (or atom -v)
```

### Overwriting an existing Ruby installation

You may already have an old version of Ruby installed. In this case, it may be easiest to update your Ruby version with [RVM - Ruby Version Manager](https://rvm.io/rvm/install#basic-install). The stable option will install RVM with the latest stable \(tested and approved\) version of Ruby.

```text
\curl -sSL https://get.rvm.io | bash -s stable --ruby
```

### RVM Cheat Sheet

Now that you have RVM, some useful commands it can perform:

```text
rvm list known
```

This lists all known versions of Ruby

```text
rvm install X.X
```

Install version X.X of Ruby \(where you replace the X's with the appropriate version number you would like to install\).

```text
rvm use X.X
```

If you have multiple versions of Ruby, you must tell your computer which one to use as the primary or default version.

```text
rvm use X.X --default
```

This does the same as the above command, but additionally sets this version of Ruby as the default for any new shells you might use.

Refer to [RVM documentation](https://rvm.io/) for any further RVM questions.