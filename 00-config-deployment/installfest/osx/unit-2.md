# Unit 2  OSX installfest

## Node

To install Node

```text
brew install node
```

Verify the installation afterwards by running

```text
node -v
npm -v
```

The above should display without any errors.

To finish up your installation, run this command to allow for global installations of npm tools.

```text
sudo chown -R $USER /usr/local/lib
```

## Postgres

**Postgres.app**

We will be using a relational database called Postgres during our class.

Download and install from [http://postgresapp.com/](http://postgresapp.com/)

Open up your `.zshrc` file in your Code editor \(`code ~/.zshrc` for VS code\) Your editor will popup with configuration settings, at the bottom of the file append

```text
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin
```

Save the file and either restart your terminal or write `source ~/.zshrc` to apply your changes. To check if it worked, type `which psql` in your terminal at which point should display:

```text
/Applications/Postgres.app/Contents/Versions/9.5/bin/psql
```

---
