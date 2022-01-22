# Optional Tools

in this Section:

* iTerm, a fancy, tircked out terminal app
* Node version Manager
* Installing postgresql with homebrew
* installing the postico postgres GUI
* installing the mongoDB GUI
* changing where your mongoDB is stored (for osx Catalina and above file permission fixes)
* Setting up mongoDB Atlas and connecting to mongosh with command aliases 
* creating python3 command aliases
* other IDE options 

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

Run the following commands in your terminal:

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

## Install Postgres GUI

Mac users can utilize **Postico**. Install here:

[https://eggerapps.at/postico/](https://eggerapps.at/postico/)

## Install MongoDB GUI

One of the most common free MongoDB GUIs is **RoboMongo**. Install here:

[https://robomongo.org/](https://robomongo.org/)

## Change where your `mongodb` data is stored

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
## MongoDB and Atlas

This guide will help you set up a cloud mongodDB database and connect to it with your mongo shell.

We will be installing and configuring [MongoDB](https://www.mongodb.com/) as well as [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). Mongo uses a 'document-oriented database' structure with very JSON-like documents and familiar javascript-like commands for database operations.

MongoDB Atlas - a cloud database service that we configure online and can be used for both deployment and local development

This installfest is adapted from Mongo DB's install instructions that can be found [here](https://docs.mongodb.com/manual/administration/install-community/) and also the [MongoDB Atlas setup instructions](https://fullstackopen.com/en/part3/saving_data_to_mongo_db#mongo-db) from [fullstackopen.com](https://fullstackopen.com/en/).

**NOTE YOU MAST HAVE MONGODB INSTALLED ALREADY**

## MongoDB Atlas

> MongoDB Atlas is a cloud hosting service provided by MongoDB. We will have to sign up for an account and configure our local machines to connect to it.

### Make an account

Signup for account [here.](https://www.mongodb.com/cloud/atlas) Please note - you will have to use Google Account for OAuth.

1. Select the "Shared Clusters" free tier. 
2. For cloud provider, select AWS and for region, whichever region is physically closest to you \(example: People on the West Coast should choose `us-west-#` \). Leave all other settings on this page at their default. 
3. You will be redirected to a Dashboard where your Clusters will be listed.

### Create and configure a cluster

\(cluster means a mongoDB that lives in the far, far away in the clouds ☁️\)

this is our todo list:

* [ ] Build your first cluster
* [ ] Create your first database user along with a password
* [ ] Whitelist your IP address
* [ ] Connect your cluster
* click the green **Create a New Cluster** button on the right hand side of the page. _PLEASE NOTE: It takes 3-5 min to make a new cluster._
* On the left hand side of the screen there is a hamburger menu. Click on **Database Access** under **Security**  on the lefthand menu and then click the big green button that says  "Add New Database User".
  * For the Authentication Method, leave it on Password. Declare a username and password under Password Authentication. This information will be hidden later in an env variable on your server. **IT IS SUPER IMPORTANT THAT YOU WRITE THIS INFORMATION DOWN**.  
    * _PLEASE NOTE - the fewer special characters your password has, the easier it will be to format your URI call, but also the less secure your db will be_ 🤷  **JUST USE REGULAR CHARACTERS FOR THIS TUTORIAL -- THE SIMPLER THE PASSWORD IS THE BETTER**. 
  * Leave all other defaults the same and add user. 
* click on **Network Access** under **Security**  on the lefthand menu and then click the big green button that says  "Add IP Address".
  * For the sake of this app we are going to allow for access from anywhere since you will each be doing your own Heroku deployments. Click "Allow Access from Anywhere" under "Whitelist a connection IP address." Leave the default `0.0.0.0/0` call, and click "Add IP Address."

    ode example", and then copy the code MongoDB has created for you into a text file for use in just a moment. 

### Connecting to Your Cluster from the terminal

We are going to test the connection from our terminal to your Atlas cluster with a very long command, and then create a shell alias for this command.

#### Connecting to your Cluster

1. Return to the Clusters dashboard by clicking **Clusters** under **Data Storage** on the lefthand menu. 
2. On your Cluster, click the Connect button. 
   * Click "Choose a connection method", and on the next page choose "Connect with the mongo shell."
   * Select 'I have the mongo shell installed' and if you need to check your mongo version, there are instructions on how to do so.
3. Copy the command it gives you to connect to your mongo shell to your atlas cluster and paste it into your terminal
   * the terminal will prompt you for a password **THIS IS THE PASSWORD FOR YOUR CLUSTER'S USER THAT YOU CREATED EARLIER**
   * the command will look something like this:

     ```bash
     mongo "mongodb+srv://< your cluster name >.9hqnh.mongodb.net/< your database name >" --username < your user name >
     ```

If you are able to connect to your cluster, you are ready for the next step, otherwise take a second to debug before moving on.

#### Alias the Atlas connection command

That giant command to connect to Atlas is way to big, lets make a shorter command Alias for it in our zshell config file.

1. Open your zhell config file with in vscode with `code ~/.zshrc`
2. Scroll down to the command alias section and add the following line, but replacing this generic command with the one you ran from the previous section:

   ```bash
   # alias for connecting to MondoDB Atlas
   alias mongo-atlas='mongo "mongodb+srv://< your cluster name >.9hqnh.mongodb.net/< your database name >" --username super_cool_person'
   ```

   _NOTE:_ You must put single quotes `' '` around the command like above

3. Save your `.zshrc` file and restart your terminal. You can now use the command `mongo-atlas` to connect to your Atlas database.

You can use the command `mongo` to connect to your local development database and the command `mongo-atlas` to connect to your Atlas cloud database.

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

# Sublime Packages

## Setting up User Settings

* Open Sublime Text
* Go to `Sublime Text -> Preferences -> Settings - User`
* Replace the file with the settings object below:

```text
{
  "rulers":
  [
    80
  ],
  "tab_size": 2,
  "translate_tabs_to_spaces": true,
  "scroll_past_end": true
}
```

## Setting up Package Control in Sublime Text

* Open Sublime Text
* Bring up the console
  * Use CTRL + \` on OSX
  * or `View > Show Console`
* Go to [https://packagecontrol.io/installation](https://packagecontrol.io/installation) and paste the appropriate code into your Terminal
  * You should be using Sublime Text 3, so copy the Sublime Text 3 code.
* Restart Sublime

#### Install Sublime Packages

* Type `COMMAND + SHIFT + P` to open the Command Palette
  * `CTRL + SHIFT + P` on Linux
* Type `Install Package` and select the first result \(by pressing `ENTER`\)
* Type the package you want to install, and press `ENTER` to begin installation.

### Useful Packages that you should install

* ColorPicker \(pick colors by typing `COMMAND + SHIFT + c`, handy for CSS\)
* Color Highlighter \(visually displays colors for hex/rgb values\)
* EditorConfig \(reads configuration files for your editor\)
* GitGutter \(shows git additions/deletions\)
* Terminal \(launch a terminal window from a folder on the sidebar\)
* BracketHighlighter \(highlight brackets and tabs\)
* Bootstrap 3 Snippets \(tab snippets for Bootstrap 3 elements\)
* EJS \(syntax definition, we'll use this when working with Node\)
* Sass \(syntax definition, we'll use this when working with Rails\)
* Babel \(syntax definition, we'll use this when working with React\)
* JSX \(syntax definition, we'll use this when working with React\)

Feel free to install any others, and we'll install others throughout the course.

**Important Note: It is not recommended that you install anything that auto-formats or "prettifies" your code. These are generally hindersome to beginners for learning basic indentation and often are not built well which ends up causing a lot of errors. Do not use these!**

### Creating a Snippet \(Optional\)

We'll use a lot of snippets when working with Bootstrap, and you can make your own as well.

* Go to `Tools > New Snippet`
* Include the content of your snippet inside `<![CDATA[ ]]>` within the `<content>` element.
* To define how to trigger the snippet, uncomment the `<tabTrigger>` line and type the keyword for your tab trigger.
* To trigger the snippet only on certain files \(for example, only HTML, or only JavaScript\), uncomment the `<scope>` tag and change the scope to the language you need.
* More details and advanced functionality can be found in [this handy blog post](http://www.hongkiat.com/blog/sublime-code-snippets/)

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