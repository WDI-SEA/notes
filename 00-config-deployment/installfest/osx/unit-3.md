# Unit 3  OSX installfest

## Installing MongoDB \(Updated 2/2021\)

**Notes:** The name of the free version of MongoDB has changed to `mongodb-community` as of November 2019. Also, the Catalina version of MacOS \(version 10.15\) disallows folders being created at the root of the file system so you must create your MongoDB data folder inside your home folder

```bash
# Download the official Homebrew formula for MongoDB and the Database Tools
brew tap mongodb/brew

# Install MongoDB
brew install mongodb-community
```

There are two ways to start your server: 1. As a macOS service 2. Manually as a background process

**As a Service**

```text
# List all services and their status
brew services ls

# Start
brew services start mongodb-community

# Stop
brew services stop mongodb-community

# Restart
brew services restart mongodb-community
```

**As a Background Process**

```text
# For Mac running Intel processors
mongod --config /usr/local/etc/mongod.conf --fork

# For Apple M1 processors
mongod --config /opt/homebrew/etc/mongod.conf --fork
```

To stop the background process, you'll need to connect to your `admin` database in your mongo shell and run `db.shutdownServer()`.

```text
> use admin
> db.shutdownServer()
> exit
```

---