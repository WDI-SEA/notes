# Unit 1  OSX installfest

---

## Unit 1

For the first portion of the class, we'll be working exclusively inside of the browser. We'll be installing the following tools.

* Slack
* zsh (if necessary)
* Homebrew
* X-code (if necessary)
* Git
* **I**ntegrated **D**evelopment **E**nvironment _\(VS Code\)_

### Slack

We will be using slack to communicate throughout the course. You should've received an invite to our channels via e-mail. You can login via the web browser, but downloading / installing the app is highly recommended.

[Download Slack](https://slack.com/downloads)


### Homebrew

Homebrew is a command line interface package manager that we will use to install various development tools in our class.

Open up your terminal app and paste the following command into it to install homebrew:

```text
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
If you need to, you can visit the [homebrew website](https://brew.sh/) for more details.

You may be prompted to install XCode command line tools. When prompted, click yes and your homebrew installation will continue.

After the installation process, run the command `brew doctor`. If any warnings or errors are displayed, we will need to resolve them before proceeding with the rest of the install fest.

### Xcode (if prompted)

We do not use Xcode in class but some other applications that we do use require some Xcode libraries. Normally, all you need is the Xcode CLI which should have already been installed when you installed Homebrew. If it didn't get installed, you can use this command:

```text
xcode-select --install
```

If you need to, you can install Xcode through the App Store. [Link here](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)

### zsh

A shell is a text interface into our computer, and we will be using a lot to run commands.

Zshell is the defualt mac shell these days, but if you don't have it (or aren't sure) you can install it with the command:

```text
brew install zsh
```

Don't worry, if homebrew noticed you already have it installed running this command won't cause any problems.

If it prompts you to change your default shell to zsh, select yes! When it asks you for your password, enter your computer user password \(it wont show up, but iTerm is keeping track of your keystrokes\).

If you are not asked about changing your shell, and you still have a `$` at the beginning of your prompt(meaning your shell is still bash), run the following command and then enter your password: 

```text
chsh -s /bin/zsh
```

You can check to see if it worked with this command:

```text
echo $SHELL
```

### oh-my-zsh

Oh my ZSH?!!! We will be tricking out commandline even further with [Oh-My-Zsh](https://github.com/robbyrussell/oh-my-zsh). iTerm2 and zsh give you all the functionality your heart can desire, but oh-my-zsh is the real life of the party. It is used to easily configure the look and feel of your command line.

Copy and past the following command into your terminal to install oh-my-zsh:

```text
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Restart your terminal, and you should see a brand new and colorful command prompt.

### GIT

Before we do this process, please make sure you have signed up for an account on [Github](http://www.github.com). We will be installing a version of GIT from home brew and also configuring it.

We will be installing a version of git from homebrew.

```text
brew install git
```

after git is installed run the following command to check your git version:

```text
git --version
```

If it is anything less than 2.30.0, run the following command to get the latest version:

```text
brew upgrade git
```

**Configuring GIT**

Using your email credentials for GIT, run these commands with your user and email configured.

```text
git config --global user.name "YOUR-USERNAME"
git config --global user.email "YOUR-EMAIL-ADDRESS"
git config --global push.default simple
git config --global credential.helper cache
```

**Setting up Github Personal Accress Token**

We are going to to use need to generate a personal access token on github that will allow us to interact with github using the CLI more easily. 

Follow the [directions found here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to create a person access token.

Once you have your personal access token, the next time git askes you for your password in your terminal, you can use the token instead to configure git.

<!-- 
**Setting up SSH Key (if prompted)** 

You might find your self having to re-authenticate GIT every time you work on your command line. Setup SSH Keys to let Github remember your machine in the future.

* [Github Generating SSH Keys](https://help.github.com/articles/generating-ssh-keys/) 
* -->

### Install VS Code

Currently the most popular editor according to developer polls. This is Microsoft's free version of Visual Studio.

Run the following command to install vscode with homebrew:

```text
brew install --cask visual-studio-code
```

vscode will appear in your applications folder when the installation is completed 

You can also download and install VS Code from [here](https://code.visualstudio.com/download)

---