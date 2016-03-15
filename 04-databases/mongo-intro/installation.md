#Installation

Before we can begin we need install the MongoDB server. We can simply install it from brew, but then we also need to create a data directory and take ownership of it so MongoDB will have access to it.

```
#Update Homebrew
brew update

#Install MongoDB
brew install mongodb

#make data directory
sudo mkdir -p /data/db

#get your user name
whoami

#set data directory permissions
sudo chown -R USERNAME:wheel /data
```

###Starting and Stopping

We have to remember to start and stop our MongoDB server.

```
#Start the MongoDB server
mongod
```

Press `control-c` to stop the server.
