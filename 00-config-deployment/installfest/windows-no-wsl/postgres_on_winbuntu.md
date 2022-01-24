## Requires a working Ubuntu setup under WSL

### Install the Service
sudo apt update

sudo apt install postgresql postgresql-contrib

### Start the Service
sudo service postgresql start

### Create a sample db (text in &lt; &gt; brackets indicates a value that you choose.  the brackets should be left out)
sudo -u postgres psql

create database &lt;dbname&gt; ;

### Create a user and grant permissions (text in <> brackets indicates a value that you choose.  the brackets should be left out)
create user &lt;username&gt; with encrypted password '&lt;password&gt;';

grant all privileges on database &lt;dbname&gt; to &lt;username&gt; ; 

### Going Forward
When starting the Ubuntu shell, you will need to start the service using sudo service postgresql start
(need to look at an init mechanism so PG starts on its own)
