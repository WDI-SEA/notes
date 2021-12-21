# Windows PC Installfest

Follow these instructions, along with an instructor, to install all of the software and tools we use during SEI on your Windows PC. **Some of these steps are complicated and will require you to work slowly and deliberately. Do not move on to the next step until your instructor has asked you to.**

There will be a few differences between your experince as a Windows user and the experiences of devs using Mac or Ubuntu. Most of these differences will be minor, but a few will be considerable and should be taken note of. As these come up during the course, please remember to refer back to this document as a reference.

## Initial Setup

1. Our first step will be installing the code editor you will be using throughout SEI, [VSCode](https://code.visualstudio.com/download). Download the installer from that link and run it to install VsCode.

2. Next, we will install [Git for Windows](https://gitforwindows.org/), which will allow us to, unsurprisingly, use git on Windows! Follow that link and download **Git for Windows**. Once downloaded, run the installer follow the onscreen instructions **with the help of your instructor.** Set the **default branch** to **main**. Select **VSCode** as the default **commit** editor.

3. If you haven't done so already, go to [GitHub](http://www.github.com) and create
an account; be sure to write down your username and password somewhere, since
we'll be using these credentials later. Next, go to [GitHub Enterprise](https://git.generalassemb.ly) and create an account. It is recommended that you use the same username. This will be the source of your learning material throughout SEI, while your personal Github will be where you showcase your projects.

1. Run the command below in your terminal. This script should be run from the root of this installfest repository.

    ```bash
    scripts/git.sh
    ```

1. Next, log into GitHub.com, go to [https://github.com/settings/ssh](https://github.com/settings/ssh)

1. Click the `New SSH key` button at the top right of the page

1. Enter a title for your SSH key (you can call it whatever you want)

1. Paste in your SSH key!

1. Click the `Add SSH key` button

1. Hit [Enter] in your Terminal to continue!

1. Next, log into git.generalassemb.ly, go to [https://git.generalassemb.ly/settings/keys](https://git.generalassemb.ly/settings/keys), and paste in the same SSH key.

1. You've now finished the initial setup! Great work!

## Node Setup

We're going to be installing Node. Node (and its various packages) will be the foundation of a large part of the course.

### NVM (Node Version Manager)

First, we're going to install a tool called [NVM for Windows](https://github.com/coreybutler/nvm-windows#node-version-manager-nvm-for-windows) that allows us to maintain multiple different versions of Node, in case we want to switch between them for different projects. The original NVM is only available for Mac/Linux, this is an alternative with the same functionality.

1. Follow the above link and click *Download Now*. Under the heading 1.1.7 - Maintenance Release download nvm-setup.zip.

2. Unzip the file and **run** the installer **as Administrator** with the instructor.

3. Close and reopen your terminal.

4. Next run these commands, one at a time, in the terminal.

    ```sh
    # installs a specific version of node
    nvm install 16.2.0
    # sets that version for current shell
    nvm use 16.2.0
    # sets that version as the default
    nvm alias default 16.2.0
    ```

### NPM Packages

Now, we will use Node's associated package manager, `npm`, to download and install some Node modules and make them available across all of our projects.

Run this command in your terminal.

```sh
npm install --global jsonlint eslint grunt-cli remark-lint phantomjs-prebuilt nodemon node-sass
```

Once that is finished running, the Node setup is complete!

## Python Setup

Now we'll install the [Python](https://www.python.org/downloads/release/python-377/) language onto your computer. We will also be installing a package that will help us install other Python things called `pip`.

1. Follow the above link, scroll to the *Files* section, and download the `Windows x86-64 executable installer`.

2. Run the installer with your instructor, making sure to click the **Add Python 3.x to PATH** checkbox.

3. Close your Terminal and reopen it

4. Run this command in your terminal to install some of the tools we will be using with Python.

    ```sh
    pip3 install pipenv pylint
    ```

5. Finally, we will be creating an alias (kind of like a nickname for a command) for running Python. Git for Windows does not like to open Python the way we'd like it to, so we're going to create a file (.bashrc) and add a line to it to tell our terminal exactly how to run Python from now on. Run these commands in your terminal:

    ```sh
    cd ~

    touch .bashrc

    code .bashrc
    ```

6. Next paste in the following, making sure to replace `<user>` with your Windows user.

    ```sh
    alias py="C:/Users/<user>/AppData/Local/Programs/Python/Python37/python.exe -i"
    alias python='winpty python.exe'
    ```

7. Close and reopen your terminal **x2**.
    >**Note: Our friends using Mac and Ubuntu will use the command `python3` to run the Python shell. We will be using the command `py` to do the same thing.**

## Important Libraries

Next we're going to be installing two very important libraries that work alongside some of the tools we've already installed. `Libsass` and `tidy-html` will give us access to functinality we did not have previously.

### Libsass

Installing `libsass` is the easier of the two, so we'll start there.

1. Run the following command in your terminal:

    ```sh
    pip install libsass
    ```

2. You're finished!

### Tidy-html

Installing `tidy-html` is going to be a bit more involved than `libsass` and we're going to have to use a couple tools that we probably won't be using for the rest of the course.

The first is PowerShell, a special Windows terminal. The second is a package installer, called [Chocolatey](https://chocolatey.org/) that runs inside PowerShell. Let's get started.

1. First, type `powershell` in the Windows search bar and right click on PowerShell and select **Run as Administrator**.

2. Run the following command in PowerShell. When prompted type `"A"` to run all:

    ```sh
    # this command allows us to install programs via PowerShell
    Set-ExecutionPolicy Bypass -Scope Process
    ```

3. Next we will run another command in PowerShell to install Chocolatey. Make sure to copy and paste this exactly how it is.

    ```sh
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    ```

4. Once the install finishes, we will run one last command to install `tidy-html`:

    ```sh
    choco install html-tidy
    ```

5. When that is done, close PowerShell and then close and reopen your terminal.

## VSCode Packages

1. Install code packages


```sh
code --install-extension dbaeumer.vscode-eslint \
  --install-extension esbenp.prettier-vscode \
  --install-extension christian-kohler.path-intellisense \
  --install-extension streetsidesoftware.code-spell-checker \
  --install-extension ms-python.python \
  --install-extension dbaeumer.vscode-eslint \
  --install-extension mikestead.dotenv \
  --install-extension mkaufman.HTMLHint \
  --install-extension ecmel.vscode-html-css \
  --install-extension steve8708.Align \
  --install-extension yzhang.markdown-all-in-one \
  --install-extension esbenp.prettier-vscode \
  --install-extension sibiraj-s.vscode-scss-formatter \
  --install-extension EditorConfig.EditorConfig \
  --install-extension CoenraadS.bracket-pair-colorizer-2 \
  --install-extension capaj.vscode-standardjs-snippets \
  --install-extension jaspernorth.vscode-pigments \
  --install-extension formulahendry.auto-close-tag
```

2. Enable autosave by going to `File`. Then make sure the `Auto Save` option in the dropdown is selected. 

## Chrome Setup

1. Download Google Chrome if you haven't already.
2. Update your chrome settings to [match this image](chrome.md)

## MongoDB Setup

### Install MongoDB

We'll now install MongoDB, another open source database. To do so, we will follow the install steps [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/#install-mongodb-community-edition).

### Add MongoDB Aliases

Once those have been completed we will follow the steps [here](https://teamtreehouse.com/community/how-to-setup-mongodb-on-windows-cmd-or-gitbash-with-shortcuts) to set up MongoDB to work with our terminal.

### Install MongoDB Tools

1. Go to the [mongo tools download page](https://www.mongodb.com/try/download/database-tools?tck=docs_databasetools)
2. Under **package type** select **msi** (so an installer is downloaded)
3. Click download and install mongo tools
4. Navigate to the mongo tools `bin` folder (ex. `C:\Program Files\MongoDB\Tools\[version]\bin`)
5. Copy the path to the **mongo tools bin** folder
6. Edit the user's **Path** environment variable and add the path to the **mongo tools bin** folder 

## PostgreSQL Setup

We will be installing PostgreSQL, an open source relational database management system. In SEI, we will be writing SQL (structured query language) and maintaining our relational databases using Postgres.

On Windows we will be following [this tutorial](https://medium.com/@itayperry91/get-started-with-postgresql-on-windows-a-juniors-life-4adfa6dd10e) to setup Postgres. You'll need to select the version in the installer.

## Django Environment Setup

This script will create two new folders on your machine: sei and a sub-folder django-env.

The final folder structure will look like this:

```
~/sei
├── django-env
```
The django-env folder will be used to hold the Pipenv virtual environment and dependencies we'll need to work with the Django framework.

In your terminal, run:
```
mkdir -p ~/sei/django-env
cd ~/sei/django-env
pipenv shell "pipenv install django psycopg2-binary; exit"
```

# Congratulations, you have finished Installfest!

## Troubleshooting

### VSCode

#### code command not found

If this occurs, add the `bin` directory of your `code` download to your PATH environment variable.

### NVM (Node Version Manager)

#### space in username

If you have a space in your username you can see errors like:

> "C:/Users/Example" is not a valid command

To solve this error, you'll want to use your `shortname` in paths instead.

1.  Run [`dir /x` from the `Users` directory](https://github.com/coreybutler/nvm-windows/issues/405#issuecomment-633395759) to locate shortname
1.  Then get to `AppData` folder (you can do `%AppData%` in the file search bar to reach the roaming folder)
1.  Go into `nvm` folder and [open `settings.txt` and replace  the `root:` definition](https://github.com/coreybutler/nvm-windows/issues/405#issuecomment-626359211) so it uses the short name

Here are

#### No app associated with this application

1.  on `nvm use` step we get an error pop up "No app associated with this application something something". If this occurs, make sure you installed `nvm` as an `Administrator`.
