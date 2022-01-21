# Installing & Configuring Git
If your computer doesn not have git installed, run `sudo apt-get install git`

## Github Personal Access Tokens

Beginning in 2021, you cannot directly interact with code repositories stored on Github.com through the command line. You must set up Personal Access Tokens (PAT) and paste them to your terminal or use Command Line tools like Git Credential Manager to manage access to Github repos.

**Below are 3 different strategies for connecting to Github. Ask your class team which method they will prefer.**
- PAT Tokens
- Git Credential Manager Core
- Setting Up SSH Keys

[You can follow Github's directions for generating a PAT here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token#using-a-token-on-the-command-line). **Be sure to have your PATs generated and readily available at the start of each working day.**

[Alternatively, you can cache your GitHub credentials using GCM Core and get access through your terminal.](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git). You would follow the Linux directions instead of the Windows Tab, as this guide is for Windows Subsystem Linux.

## Setting Up SSH Keys
[Your class team may also plan to use SSH Keys as an alternative to Personal Access Tokens, too!](https://docs.github.com/en/enterprise-server@3.0/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

## Configuring a Global git ignore

> Note: This is **IMPORTANT**

Everyone should have a global **git ignore** file so that you don’t have to worry about making the appropriate entries in a project’s git ignore.

First, create the file:  `touch ~/.gitignore_global`

Next, configure git to use this file:  `git config --global core.excludesfile ~/.gitignore_global`

Finally, lets put some good stuff in there by editing the newly created `.gitignore_global` file using VS Code:

1. `code ~/.gitignore_global` to open the file in VS Code

2. Copy/paste the following:

	```sh
	# This is a list of rules for ignoring files in every Git repositories on your computer.
	# See https://help.github.com/articles/ignoring-files
	
	# Compiled source #
	###################
	*.class
	*.com
	*.dll
	*.exe
	*.o
	*.so
	
	# Packages #
	############
	# it's better to unpack these files and commit the raw source
	# git has its own built in compression methods
	*.7z
	*.dmg
	*.gz
	*.iso
	*.jar
	*.rar
	*.tar
	*.zip
	
	# Logs and databases #
	######################
	*.log
	
	# OS generated files #
	######################
	._*
	.DS_Store
	.DS_Store?
	.Spotlight-V100
	.Trashes
	ehthumbs.db
	Thumbs.db
	.vscode

	# Testing #
	###########
	.rspec
	capybara-*.html
	coverage
	pickle-email-*.html
	rerun.txt
	spec/reports
	spec/tmp
	test/tmp
	test/version_tmp
	
	# node #
	########
	node_modules
	
	# Rails #
	#########
	**.orig
	*.rbc
	*.sassc
	.project
	.rvmrc
	.sass-cache
	/.bundle
	/db/*.sqlite3
	/log/*
	/public/system/*
	/tmp/*
	/vendor/bundle
	
	
	# Ruby #
	########
	*.gem
	*.rbc
	.bundle
	.config
	.yardoc
	_yardoc
	doc/
	InstalledFiles
	lib/bundler/man
	pkg
	rdoc
	tmp
	
	# for a library or gem, you might want to ignore these files since the code is
	# intended to run in multiple environments; otherwise, check them in:
	# Gemfile.lock
	# .ruby-version
	# .ruby-gemset
	
	# CTags #
	#########
	tags
	
	# Env #
	#######
	.env
	
	# Python #
	#######
	*.pyc
	__pycache__/
	```

3. Save the file.

## Avoiding Having to Create A Git Message Every Time a Git Merge Takes Place

By default, git asks for a commit message any time a merge takes place, for example, you'll be running this command quite a bit:  `git pull upstream master`.

To avoid this from happening, we can add a single line to our terminal configuration - this is the line we're going to need to add anywhere inside of the file identified below:

```
export GIT_MERGE_AUTOEDIT=no
```

**If NOT using ZSH:**

Use VS Code to edit the `~/.bash_profile` file:

```
code ~/.bash_profile
```

**For ZSH users:**

Use VS Code to edit the `~/.zshrc` file:

```
code ~/.zshrc
```

**Regardless of which file you edited, be sure to save it.  You will also need to quit the terminal and relaunch it for this setting to take effect.**

Next up: Setting Up Languages and Frameworks!
* [X] [Command Line](command-line-setup.md)
* [X] [Configuring Git](git-configuration.md)
* [ ] [Databases and Frameworks](dbs-languages-frameworks.md)
* [ ] [Desktop Applications](desktop-applications.md)
