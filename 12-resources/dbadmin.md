# Database Administration

**This guide explains the following:**

* Postgres - Local - backup / restore
* Postgres - Heroku - backup / restore
* Mongo - Local - backup / restore
* Mongo - Heroku - backup / restore
* Accessing production databases
  * Mongo / Postgres GUI options

**IMPORTANT NOTE:** This document is currently in beta, but should give you a good starting point for backing up data, restoring data, and accessing production databases.

## Postgres - Local

Remember you need to have your local postgres server \(the elephant icon on mac\) running for any of these commands to work.

### Backup postgres database to file

This will create a file named `db.sql` which will contain all of the data of the local postgres database named `APP_DATABASE_NAME` change these names to match your app as needed.

This is useful for sending to your teammates if you're collaborating or just to have a backup incase you break something.

```text
pg_dump -s -c APP_DATABASE_NAME > db.sql
```

The `-s` flag is for schema only. If you want your development data included just remove that flag.

The `-c` flag tells it to drop old data before creating new data. This is just incase you've done this more than once and are overwritting existing data.

### Restore postgres file to database

This will create a database named `APP_DATABASE_NAME` using the data in `db.sql`. It will **DESTROY** the database if it already exists.

```text
psql -d APP_DATABASE_NAME < db.sql
```

This will throw some errors if the dump was created by someone else. It is ok to ignore these errors.

### Reset local database

For the restore process to work you need to have an empty database. The easiest way to achieve this is to just drop and re-create the database.

Make sure there is nothing actively connected to the database \(pgCommander, rails, node, etc\) when you do this or it won't work.

**Delete the database**

```text
dropdb APP_DATABASE_NAME
```

**Create a new empty database**

```text
createdb APP_DATABASE_NAME
```

## Postgres - Heroku

### Push existing .sql file to heroku

If you already have a `.sql` file you want to upload to heroku you can use this command.

```text
heroku pg:psql < db.sql
```

### Push / Pull database to / from Heroku

Heroku also has commands that will allow you to transfer your local database to heroku or vise-versa without needing to create a `.sql` file.

### Push database to heroku

Uploads the local database named `APP_DATABASE_NAME` to heroku using the `heroku config` value for `DATABASE_URL`.

```text
heroku pg:push APP_DATABASE_NAME DATABASE_URL
```

### Pull database from heroku

This will download the database using the `heroku config` value for `DATABASE_URL` and store it in the database named `APP_DATABASE_NAME`.

```text
heroku pg:pull DATABASE_URL APP_DATABASE_NAME
```

### Reset database

Before you can push a database to heroku you must clear the old database \(if one exists\).

```text
heroku pg:reset DATABASE_URL
```

## Mongo - Local

Remember you need to have `mongod` running to do any database manipulation.

### Backup mongo database to file

This will create a folder called `dump` and backup the contents of the mongo database `APP_DATABASE_NAME` in that folder.

```text
mongodump -h 127.0.0.1 -d APP_DATABASE_NAME -o dump/
```

### restore mongo database from file

This will create a mongo database named `APP_DATABASE_NAME` by using the dump named `APP_DATABASE_NAME` in the dump directory.

```text
mongorestore -h 127.0.0.1 -d APP_DATABASE_NAME dump/APP_DATABASE_NAME
```

* `-h` set host to local host.
* `-d` target database name \(database to create\)
* `dump/APP_DATABASE_NAME` source dump file to import \(listed as last parameter\)

## Mongo - Heroku

### Push existing dump to heroku

```text
mongorestore -h xyz.mongolab.com:12345 -d remote_db_name -u username -p password dump/mylocal_db_name/
```

you can get the details for mongorestore from the mongo connection uri by running `heroku config` to get the mongo connection uri. It will be in the followin format.

```text
MONGOLAB_URI: mongodb://username:password@server:port/remote_db_name

# which will look kinda like this:

MONGOLAB_URI: mongodb://heroku_abcdefg:abcdefghijklm@xyz.mongolab.com:12345/heroku-13411
```

## Production Database Access

### Postgres

Your local database is only for local testing. Your production database is hosted by heroku so if we want to see what is going on in the database we need to connect to it. To get the database connection details run `heroku config` and copy the database connection string \(starts with "postgres://"\). With that url in your clipboard load PG Commander and click "New Favorite" and it will automatically populate the connection fields.

If you aren't using PG Commander you'll have to manually enter the parts of the connection string. The format is as follows:

```text
postgres:// USER_NAME : PASSWORD @ SERVER_URL : PORT_NUMBER / DATABASE_NAME

It'll look kinda like this (heroku passwords tend to contain a hyphen):
postgres://xxxxxx:yyyyyyy-zzzzzzzz@ec2-54-83-55-214.compute-1.amazonaws.com:5432/abcdefghijklmnop
```

**Postgres GUIs**

* [PG Commander](https://eggerapps.at/pgcommander/)
* [PG Admin](http://www.pgadmin.org/)

### Mongo

The steps for mongo are the same except the url will start with `mongodb://` and you'll be setting it up in your mongo gui instead of PG Commander.

You'll need to click "create" to create a new connection and manually enter the connection details from `heroku config` which will be in the following format.

```text
MONGOLAB_URI: mongodb://username:password@server:port/remote_db_name

# which will look kinda like this:

MONGOLAB_URI: mongodb://heroku_abcdefg:abcdefghijklm@xyz.mongolab.com:12345/heroku-13411
```

**Mongo GUIs:**

* [RoboMongo](http://robomongo.org/)
* [Mongo Hub](https://github.com/jeromelebel/MongoHub-Mac)

