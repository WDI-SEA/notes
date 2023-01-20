# WSL Unit 2, 3, and 4 installfest

**Stop!** The following instructions pertain to units 2-4 - revisit this section in unit 2!

## Node.js

We're going to install Node.js using a tool called Node Version Manager \(NVM for short\). Node has been around for a while and has many versions available for us to use. We're going to focus on the latest Longterm Support \(LTS\) version for our work in the course.

1. Run the following command to download and run the `nvm` install script via `curl`:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```

* _**Important Note**_! If you've installed or plan to install Zsh and use that instead of bash, you will need to come back and run the following command after having installed Zsh:

  ```bash
  # Run this command instead if you're using Zsh
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | zsh
  ```

* Double check that NVM installed correctly with:

```bash
nvm --version
```

1. Finally we're ready to install Node. We want the latest LTS version. To get it and use it, run these commands:

```bash
nvm install --lts
```

> Your console should display a progress bar during installation. Wait for this to complete before continuing.

1. Use the lts version of node.

```bash
nvm use --lts
```

1. Set the default Node version.

   ```bash
   nvm alias default node
   ```

## Unit 2 - PostgresQL

When it comes to installing database technologies - WSL has a handful of extra configuration steps as the installations will not work by default.

* [PostgresQL Webpage](https://www.postgresql.org/download/linux/ubuntu/)

```bash
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

`psql: error: FATAL: role "<your_user_name>" does not exist`

## The fix:

* Run the following commands one by one, but change `<your_user_name>` to your linux username!

```bash
# Auto start the postgres server
sudo -u postgres pg_ctlcluster 13 main start

# Start the postgres server the first time
sudo service postgresql start

# Create a postgres user that matches your username
sudo -u postgres createuser <your_user_name>

# Create a postgres database that matches your username
sudo -u postgres createdb <your_user_name>

# Run psql as the postgres user
sudo -u postgres psql
```

* The last command will bring you inside of the `psql` shell - run the following command

```text
ALTER USER <your_user_name> WITH SUPERUSER;
```

## Unit 3 - MongoDB

When it comes to installing database technologies - WSL has a handful of extra configuration steps as the installations will not work by default.

* Run the following commands one by one:

```bash
sudo apt install mongodb
sudo service mongodb start
```

* Test if it worked by running the `mongo` command, and also try the `mongosh` command. If you are in the mongo shell, then it worked!
* If it didn't work, and you get an error referring to `/data/db` - run the following:

```text
sudo mkdir -p /data/db
sudo chmod 777 /data/db
mongod --dbpath /data/db
```

## Unit 4 - Python

Python install instructions - run the following commands in your terminal

```bash
# install python
sudo apt-get install python3
sudo apt-get install python3-pip
```

In your `~/.zshrc` file, add the following lines

```bash
# Alias python to python3
alias python=python3
alias pip=pip3

# To allow pip packages to be in PATH
path+=(/home/<your_user_name>/.local/bin)
```

## Navigation

1. Read this intro
   * \[✔️\] [Alternative OS intro](./)  
2. Prior to the first day of class: Enable WSL and Install Ubuntu from the Microsoft Store app
   * \[✔️\] [WSL Setup](wsl-setup.md)
3. On the first day of class, your instructors will help you with **Installfest**
   * \[✔️\] [Installfest](wsl-installfest.md)
4. Optional visual and usability upgrades for your terminal
   * \[✔️\] [Upgrades](upgrades.md)
5. Unit 2-4 Installfest
   * \[✔️\] [Unit 2, 3, 4 Installfest](wsl-unit234.md)

