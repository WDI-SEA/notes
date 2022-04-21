# Software Engineering Immersive WSL2/Linux Installfest Guide (UPDATED FOR 2022!)

## Table of Contents
- How to use this guide/FAQ 
- What will be installed on my computer?
- Installing WSL2 on your Windows Computer
- Setting up your WSL2 environment for SEI
- Instructors/Staff Notes


**DISCLAIMER: This information is provided as-is. You are personally responsible for the effects installing WSL on your computer may have. This document is an open-source project and subject to continued updates.**

## How to use this guide
I wrote this guide in response to the growing number of General Assembly students and staff using Linux Computers. I wanted to create a standardized dev environment that would allow compatible Windows computer users to fully participate in SEI and not worry about finding matching Windows equivalents for tools used in SEI. 

Setting up a working dev environment is important for success later in the full-stack sections of the course. While Macbooks are the most recommended computers, I wanted to create a resource that proves the viability of using other, more affordable, computer systems.

Windows Subsystem Linux 2, or WSL2 for short, creates an instance of a Linux operating system running on a Windows computer. The advantages of performing tasks inside this embedded system are explained in detail later in this guide. Setting up a Dev Environment with WSL2 allows Windows computer users to seamlessly work with students and instructors using Mac or Linux. 

**While this guide is designed for setting up WSL2 on Windows computers, these instructions can also be followed for setting up a computer already running Ubuntu Linux. Simply run terminal installation commands that start with sudo for installing software during some sections like MongoDB and Django.**

## What will be installed on my computer?
- Windows Subsystem Linux 2
- Ubuntu Terminal
- Zsh (with Oh-My-Zsh configuration)
- VSCode (+ some optional helpful extensions)
- Git
- Node.js
- NPM 
- Python3
- Django
- Heroku CLI
- MongoDB
- PostgreSQL
- Slack (Desktop App recommended for immediate notifications!)

Please read the FAQ section before continuing to look over the installation instructions.

## FAQ
- *Why should I install WSL2 on my computer?*
   - We recommend installing WSL2 to provide a (mostly) seamless experience working with the SEI curriculum and other learning resources that were designed with UNIX-based operating systems like Linux or Mac OS. These operating systems have a different structure than Windows, and many tools used in the SEI curriculum are best managed with a UNIX OS.

- *What recommended specs/kind of Windows computer do you recommend for learning web development and software engineering?*
   - Here are some recommended specs for any computer:
      - Processor: Intel i5, Intel i7 or equivalent and above (like AMD Ryzen 5 or 7)
      - RAM: at least 8GB (12GB or more recommended for remote setting)
      - Storage: 128GB or more available storage
      - compatible with Windows 10 version 1903 or later. (see WSL2 installation instructions to check compatibility)
   - Be sure to contact your cohort's staff with this information about your computer ASAP:
      - Brand Name
      - Laptop Model No./Name (e.g Thinkpad Carbon X7 or Dell XPS (2019) 13")
      - Manufacturing Date (Year)
      - Processor
      - RAM
      - Available storage
      - Operating System (including Windows Build ver.)
   - Most premium business laptop lines from major brands like Dell or Thinkpad will meet these requirements. In general, I recommend a Lenovo Thinkpad or Dell XPS. You can also contact me if you want to double check your computer's compatiblity! :)
   - **CUSTOM PCs MAY NEED TO HAVE BIOS MODIFIED FOR COMPATIBILITY** 

- *There are Windows versions of (Git, PostgreSQL, etc.). Why do I need to use the Linux versions of tools?*
   - The version of Linux we install to our computers is treated as a separate operating system, so some tools might not be able to detect what's going on inside our WSL installation. Plus, we will mostly be using our Linux terminal to manage these tools. For example, the GIT CMD terminal you can download for Windows from Git's official website allows you to manage your git projects just like a Bash/Z-shell terminal. 
   
   - However, the GIT CMD terminal CANNOT manage other important tasks like running servers on Node.js or connecting to databases. For this reason, it is important to set up a terminal that can directly manage ALL development processes.

- *Why are we installing Django (instead of other web development frameworks like Ruby on Rails, Laravel, etc.)?*
   - We include installation instructions for Django because it is a popular web development framework using Python. Because curriculum syllabi may vary by market, Be sure to contact your class team for details about what languages and frameworks are covered. For example, some campuses might teach Ruby on Rails or Flask instead of Django. This guide does not have instructions for these tools yet. Because this document is also an open-source project, I encourage you to fork it and add on additional installation instructions if you are using another curriculum. :)

- *Can I use a chromebook for SEI?*
   - Brief answer: NO
   - More detailed answer: The curriculum will quickly become difficult if you are not able to move away from in-browser workspaces and start working with the back-end from the terminal or using front-end libraries like React or Vue.
   - We recommend getting a Linux, Mac OS, WSL computer as soon as possible to establish a working dev environment for yourself. You will need a fully-featured operating system to practice controlling your computer with the command line and using professional development tools and systems like Git or a code editor. There are guides on the Internet to setting up a dev environment on chromebooks, but we haven't found many of them to be friendly to beginners. 
   - **Chromebooks will only be allowed as secondary computers for Slack and Zoom.**

## Instructor/Staff Notes:
- This guide was designed for instructional teams where AT LEAST one staff member can set up a working software development environment, and help several dozen others set up their own and act as the liason for linux users and the class team.
- **LINUX SUPPORT CAN NOT be guaranteed if no instructional team member can be a point of contact for non-Mac using students.**
- Students considering using a non-Mac system can view this guide before deciding to use a Linux computer.
- If there are more than three students who can not use a Mac, I recommend having a pre-course Linux set-up day to ensure compatibility for Parts 1 and 2, as installing WSL to a computer can take up to three hours or more. The Database and Frameworks section and beyond take the same amount as a normal Mac SEI installfest.

## Ready to get started?
- Click through the links below installation instructions!
* [ ] [Command Line/Installing WSL2](command-line-setup.md)
* [ ] [Configuring Git](git-configuration.md)
* [ ] [Databases and Frameworks](dbs-languages-frameworks.md)
* [ ] [Desktop Applications](desktop-applications.md)
