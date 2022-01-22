# Setting Up Languages and Frameworks

## Table of Contents
- JavaScript
- Databases
  - MongoDB
  - PostgreSQL
- Python3 and Pip3
- Django
- Python Virtual Environments
- Heroku CLI  

## JavaScript (Node.js and NPM)
Run these commmands from your terminal.

- `sudo apt update`
- `sudo apt install nodejs npm`
- `sudo npm cache clean -f`
- `sudo npm install -g n`
- `sudo n stable`

Confirm installation with `node --version` and `npm --version`

## Databases (MongoDB and PostgreSQL)

The following instructions are adapted from [Microsoft's WSL Database Guide](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-database). Bookmark that page to have a quick reference for establishing connections to popular database systems.

## MongoDB

Update your Ubuntu packages: `sudo apt update`

Install MongoDB with this command: `sudo apt-get install mongodb`

Confirm installation and get the version number: `mongod --version`

After finishing the installation, run `which mongod` (yes, `mongod` with a d) to check that it's installed.

There are 3 commands you need to know once MongoDB is installed. Write these down somewhere safe when you start using MongoDB in class:

- `sudo service mongodb status` for checking the status of your database server.`
- `sudo service mongodb start` to start running your database server.`
- `sudo service mongodb stop` to stop running your database server.`

## PostgreSQL

To install PostgreSQL on WSL:

Update your Ubuntu packages: `sudo apt update`

Once the packages have updated, install PostgreSQL (and the -contrib package which has some helpful utilities) with: `sudo apt install postgresql postgresql-contrib`

Confirm installation and get the version number: `psql --version`

There are 3 commands you need to know once PostgreSQL is installed. Write these down somewhere safe when we start using these DBs in class:

- `sudo service postgresql status` for checking the status of your database.
- `sudo service postgresql start` to start running your database.
- `sudo service postgresql stop` to stop running your database.

The default admin user, postgres, needs a password assigned in order to connect to a database. To set a password:

Enter the command: `sudo passwd postgres`
You will get a prompt to enter your new password.
Close and reopen your terminal.

To run PostgreSQL with psql shell:

Start your postgres service: `sudo service postgresql start`
Connect to the postgres service and open the psql shell: `sudo -u postgres psql`
Once you have successfully entered the psql shell, you will see your command line change to look like this: 
```
postgres=#
```

To exit postgres=# enter: \q or use the shortcut key: Ctrl+D

To see what user accounts have been created on your PostgreSQL installation, use from your WSL terminal: `psql -c "\du"` ...or just `\du` if you have the psql shell open. This command will display columns: Account User Name, List of Roles Attributes, and Member of role group(s). To exit back to the command line, enter: `q`.

## Python3 & Pip3

Python3 should come with Ubuntu 18.04 and later. Please confirm by running command: `python3 --version`

To install pip3 run `sudo apt install python3-pip` and confirm its installation with `pip3 --version`

## Django

Install the python3 Django virtual environment with: `sudo apt install python3-django`

Then run: `pip3 install django`

Confirm installation with `django-admin --version`

If pip3 did not come with your Linux Distro, you can follow these instructions: https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/

If your class team is planning to use Django with virtual environments, please read the Python Virtual Environments section below.

  ### Using Postgres with Django

  When you start a Django project, you'll run into a bug that prevents you from running your server and connecting to a Postgres Database. Some scary error readout might happen, but the fix is simpler than it may seem.

  You'll probably see this error somewhere in the logs when you try to do anything in Django at first:
  ```ERROR: role YOUR_LINUX_USERNAME does not exist```

  Here's how to get rid of that message and ensure smooth slithering!
  1. Log into your Postgres terminal: `sudo -u postgres psql`
  2. In the postgres terminal, create a Postgres user with the EXACT same name as your linux username: `create user my_linux_username;`
  3. Try to start the Django server again
  
## Python Virtual Environments 
Ask your class team if they plan to run virtual environments with Django.

You can start a Python3 virtual environment with: `python3 -m venv name_of_venv`

- You may be walked through an installation by your computer the first time you run this command. It will guide you through installing any other dependences needed to run a venv (virtual env.). 

Python venvs are usually named `myenv` or `venv` instead of `name_of_venv`. If successful, your command line will also have the name of the venv, and the venv code will be stored in a folder called `lib`.

Write these commands somewhere safe:
- create venv: `python3 -m venv myenv` 
- start venv: `. myenv/bin/activate` (DON'T FORGET THE PERIOD!)
- stop venv: `deactivate` (yes, that's it. )

To download Python3 pip3 dependencies, you can use the same command as Mac OS X users: 
`python3 -m pip install -r requirements.txt`
Notice how it's pip and not pip3 in this command.

## Heroku CLI for deployment

Adapted from https://dev.to/wrightdotclick/heroku-cli-on-wsl-26fp.

Run: `curl https://cli-assets.heroku.com/install.sh | sh`

Then, confirm installation by running `heroku apps` or `heroku open`

## Python Virtual Environments 
You can start a Python3 virtual environment with: `python3 -m venv name_of_venv`

- You may be walked through an installation by your computer the first time you run this command. It will guide you through installing any other dependences needed to run a venv (virtual env.). (You may also have to prepend the installation command with `sudo` for it work successfully.)

Python venvs are usually named `myenv` or `venv` instead of `name_of_venv`. If successful, your command line will also have the name of the venv, and the venv code will be stored in a folder called `lib`.

Write these commands somewhere safe:
- create venv: `python3 -m venv myenv` 
- start venv: `. myenv/bin/activate` (DON'T FORGET THE PERIOD!)
- stop venv: `deactivate` (yes, that's it. )

To download Python3 pip3 dependencies, you can use the same command as Mac OS X users: 
`python3 -m pip install -r requirements.txt`
Notice how it's pip and not pip3 in this command.

If you are trying to deploy your app to Heroku and run into some errors, you may need to install additional default packages for Heroku to detect your project is written in Python and assign the appropriate buildpack.

`sudo apt install libpq-dev python3-dev gcc` Select `y` to run through the installation automatically.

## Instructors/Staff Notes
- Linux using students must bookmark this page in their web browsers, or instruct them to download this guide and bundle it with their class repo. Have them read it over before beginning units covering full stack web development.

* [x] [Command Line](command-line-setup.md)
* [x] [Configuring Git](git-configuration.md)
* [x] [Databases and Frameworks](db-frameworks.md)
* [ ] [Desktop Applications](desktop-applications.md)
