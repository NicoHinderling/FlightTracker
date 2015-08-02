# FlightTracker

### Backstory
*Insert Short bio*

#How to set this up Locally!

### Set up our Cassandra Database
1.) [Download](http://cassandra.apache.org/download/) Cassandra

2.) Untar, put her in /opt/, and set the other directories:

```
$ tar -zxvf apache-cassandra-2.1.8-bin.tar.gz
$ sudo mv apache-cassandra-2.1.8 /opt/cassandra  
$ sudo mkdir -p /var/log/cassandra
$ sudo mkdir -p /var/lib/cassandra
```
**_Note_ :** _You may have to change the permissions of these directories. If so, do_:

```
$ sudo chown -R _NAME_ /var/log/cassandra
$ sudo chown -R _NAME_ /var/lib/cassandra
```
3.) Add her binaries to our path:

```
$ vim ~/.bashrc
$ export PATH=$PATH:/opt/cassandra/bin (Put this in, and exit vim)
$ . ~/.bashrc
```
**And we're good to go!**

To start up the DB, type:

```
$ cassandra -f
```

If you have any issues, refer to [this](https://github.com/hsgubert/cassandra_migrations/wiki/Preparing-standalone-Cassandra-in-local-machine)!

### Clone this Repository
Before we do this, I thought I'd plug [Virtual-Burrito](https://github.com/brainsik/virtualenv-burrito)! Not necessary, but very convenient for Python projects :)

```
$ git clone https://github.com/NicoHinderling/FlightTracker.git
$ cd FlightTracker
$ pip install -r requirements.txt
$ mv credentials_example.py credentials.py
```
Now add your QPX key into the creds file. If you're unfamilar, [here](https://developers.google.com/api-client-library/python/guide/aaa_apikeys)'s how to get an API key!

And finally, simply do:

```
$ python main.py
```

Noiceeeee