# Windows WSL

## You've Got Choices

The majority of the tools we use in this course _exist_ for Windows, but many of them work slightly differently, require specialized setup, and won't include most of the specific packages and frameworks we'll use in this course.

#### There are four options for how you might proceed

### 1. Get a Mac

While this is probably not what you're hoping to do, getting a Mac is the best way to ensure that your computer doesn't get in the way of you becoming a successful developer in this course \(and beyond\). Your instructors, while helpful and knowledgeable, are less able to help you debug problems with installing tools on a Windows computer, and **your instructors cannot be your technical/installation support if you choose any of the other three options. It will be your responsibility to solve these problems; your instructors can only provide limited support.**

If getting a Mac is infeasible for you, or you want the challenge, or you're an expert user, the other available options are:

### 2. Install Linux

Because Linux and MacOS are both Unix-based systems, the tools we use in this course are also available and will work in the same ways as Macs for Linux. While your instructor still won't be able to troubleshoot installation issues, or tell you what steps to follow to install pieces of software, you will be able to run the tools used in this class.

If you're comfortable setting up your computer to dual-boot Linux, this option has been most effective for GA students in the past. Or, if partitions make you cranky, some students have been successful using VirtualBox to install a Linux VM; this is likely to cause you more issues than dual-booting and it runs significantly slower, but it requires less know-how.

If you decide this is the path for you, make sure to backup all of the important files on your computer. There is a chance that during dual-boot setup you will wipe the contents of your hard drive.

### 3. Use Windows and Git Bash

Git Bash is a tool provided by GitHub to mimic the functionality of a Unix-based system on a Windows machine. This choice will require you to investigate for yourself how to install and run each of the tools we use in the course; you'll be installing the Windows version of those tools, then attempting to use them from a combination of the Windows shell and the Git Bash shell. Some students have had success with this, one bought a Mac about halfway through the course because they had run into so many issues with the slight differences between how frameworks and applications run on the different operating systems.

### 4. Use the Windows Subsystem for Linux

Windows Subsystem for Linux \(WSL\) is a tool by Microsoft that allows you to run a Linux command line environment directly inside of Windows without having to dual-boot or run a separate VM program.

Similar to how you may have used the Git Bash terminal for your pre-work, WSL will give a you Bash terminal – but with the full power of a complete Linux distribution for development.

However, it is a tool that's actively in development, and the development experience on WSL will not be exactly the same as on a native Linux installation.

The biggest differences for our classroom use are that the installation for various tools may require additional steps, and unlike Git Bash, all of our files will live inside the WSL environment. This means that while using WSL we need to be mindful that our files exist in the Linux environment, so we will be installing and using exclusively the Linux version of tools rather than Windows tools. \(With the exception of VS Code, which is able to interoperate with WSL seamlessly\)

With that out of the way, here are the directions that will allow you to use WSL.

## WSL install instructions

1. Read this intro
   * \[✔️\] [Alternative OS intro](./)  
2. Prior to the first day of class: Enable WSL and Install Ubuntu from the Microsoft Store app
   * [ ] [WSL Setup](wsl-setup.md)
3. On the first day of class, your instructors will help you with **Installfest**
   * [ ] [Installfest](wsl-installfest.md)
4. Optional visual and usability upgrades for your terminal
   * [ ] [Visual Upgrades](upgrades.md)
5. Unit 2-4 Installfest
   * [ ] [Unit 2, 3, 4 Installfest](wsl-unit234.md)

