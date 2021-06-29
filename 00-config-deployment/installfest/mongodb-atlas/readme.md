# ![](https://upload.wikimedia.org/wikipedia/en/thumb/4/45/MongoDB-Logo.svg/2880px-MongoDB-Logo.svg.png) Mongo DB and Atlas Installfest

We will be installing and configuring [MongoDB](https://www.mongodb.com/) as well as [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). 

* MongoDB is a popular open source **NoSQL** database. 
* The MongoDB community CLI (a shell that lets us interact with our mongo database similar to `psql`)
* MongoDB Atlas - a cloud database service that we configure online and can be used for both deployment and local development

This installfest is adapted from Mongo DB's install instructions that can be found [here](https://docs.mongodb.com/manual/administration/install-community/) and also the [MongoDB Atlas setup instructions](https://fullstackopen.com/en/part3/saving_data_to_mongo_db#mongo-db) from [fullstackopen.com](https://fullstackopen.com/en/).

## Installing MongoDB

Mongo uses a 'document-oriented database' structure with very JSON-like documents and familiar javascript-like commands for database operations.

This installfest is adapted from Mongo DB's install instructions that can be found [here](https://docs.mongodb.com/manual/administration/install-community/), and the 

### Linux (and Windows WSL)

When it comes to installing database technologies - WSL and Linux have a handful of extra configuration steps as the installations will not work by default.

* Run the following commands one by one:
```
sudo apt install mongodb
sudo service mongodb start
```

* Test if it worked by running the `mongo` command. If you are in the mongo shell, then it worked!
* If it didn't work, and you get an error referring to `/data/db ` - run the following:

```
sudo mkdir -p /data/db
sudo chmod 777 /data/db
mongod --dbpath /data/db
```

### Mac OS

We will be using `homebrew`, everyone's favorite package manager, for this install.

#### Getting set up for install

You should already have the xcode command line tools installed from the unit 1 install fest, but just to be sure run the following command:

```bash
xcode-select --install
```

If you get an error, that is a good thing! It means you already have the needed tools installed. Otherwise, it can take up to 5 min or so to download the package and install it, so be patient. 

#### Installing MongoDB

Now lets install Mongo DB! Run the following two commands one after the other:

```bash
brew tap mongodb/brew

brew install mongodb-community@4.4
```

You, my friend, have just installed MongoDB! You can run `brew cleanup` to remove any tempory files used for the installation if you wish

___

Now that mongoDB is installed, you will be able to use the following commands to start/stop/restart the mongodb servies with the follwoing commands:

```bash
# start service
brew services start mongodb-community

# stop service
brew services stop mongodb-community

# restart service
brew services restart mongodb-community
```

You will need to have the mongodb service running in order to use the database -- so make sure it is started before you begin using mongodb!

#### Using the MongoDB Shell

To the mongdb shell simply type the `mongo` into your terminal. You should see a shell like this:

![mongo db shell](/mongo-shell.png)

Congrats! MongoDB is successfully installed! You can exit the shell by typing `quit()`

The mongo shell is like the `psql` but for mongoDB instead of postgres.

## MongoDB Atlas

We will be using Atlas as the host for our MongoDB database.

*Part 1 - Setting Up Atlas Account:*

### Make an account

Signup for account [here.](https://www.mongodb.com/cloud/atlas) Please note - you will have to use Google Account for OAuth. 

1. Select the "Shared Clusters" free tier. 
2. For cloud provider, select AWS and for region, whichever region is physically closest to you (example: People on the West Coast should choose `us-west-#` ). Leave all other settings on this page at their default. 
3. You will be redirected to a Dashboard where your Clusters will be listed.

### Create and configure a cluster

(cluster means a mongoDB that lives in the far, far away in the clouds ☁️)

this is our todo list:

- [ ]  Build your first cluster
- [ ]  Create your first database user along with a password
- [ ]  Whitelist your IP address
- [ ]  Load Sample Data
- [ ]  Connect your cluster

4. lick the green **Create a New Cluster** button on the right hand side of the page. *PLEASE NOTE: It takes 3-5 min to make a new cluster.* 
5. On the left hand side of the screen there is a hamburger menu. Click on **Database Access** under **Security**  on the lefthand menu and then click the big green button that says  "Add New Database User".
  * For the Authentication Method, leave it on Password. Declare a username and password under Password Authentication. This information will be hidden later in an env variable on your server. **IT IS SUPER IMPORTANT THAT YOU WRITE THIS INFORMATION DOWN**.  
    * *PLEASE NOTE - the fewer special characters your password has, the easier it will be to format your URI call, but also the less secure your db will be* 🤷  **JUST USE REGULAR CHARACTERS FOR THIS TUTORIAL -- THE SIMPLER THE PASSWORD IS THE BETTER**. 
  * Leave all other defaults the same and add user. 
6. click on **Network Access** under **Security**  on the lefthand menu and then click the big green button that says  "Add IP Address".
  * For the sake of this app we are going to allow for access from anywhere since you will each be doing your own Heroku deployments. Click "Allow Access from Anywhere" under "Whitelist a connection IP address." Leave the default `0.0.0.0/0` call, and click "Add IP Address."
7. Return to the Clusters dashboard by clicking **Clusters** under **Data Storage** on the lefthand menu. 
8. On your Cluster, click the Connect button. 
  * Click "Choose a connection method", and on the next page choose "Connect your application."
  * On this new Connect page, under list item two, click "Include full driver code example", and then copy the code MongoDB has created for you into a text file for use in just a moment. 

### Connecting to Your Cluster from the terminal

## Using Your New MongoDB tools