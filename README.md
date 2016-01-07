# :airplane: FlightTracker :airplane:

### Backstory
As a college student raised in California but studying in Boston, me having to purchase flight tickets was inevitable. Every time the topic would come up, my mom would warn me, "Buy them early! Their always cheapest several months in advance!" When I was buying a ticket for my recent trip to China, my advisor told me how "tickets are just cheapest a couple days before the flight itself!" 

I remember even Googling "`Best time to buy a Plane ticket`", which informed me that apparently _Tuesdays around noon_ are the weekly sweet spot. Well it's time to **DISPELL THE MYTHS**! 

I will be aggregating data for the next couple of months and plan to publish what I find around late December/early January!

### My Current Intentions
Try to see trends in the price fluctuation in respect to:

- Specific day of week/time of day that correlates to price
- Best “amount of time left” until flight leaves for price
- Which Company

Some other possible variables that I may encorporate in the future could be:

- Region (from which location to which location)
- Any Difference when considering Round Trip flights
- (Feel free to suggest any others! :smile: )

### Metrics
I have decided to choose two flights the day of December 19th (2015). I imagine this date should yield especially volatile prices, so it should be an interesting base line. 

**Specific Tickets:**

1.) BOS -> LAX (5/10/16)

2.) NYC -> MIA (5/10/16)

3.) NYC -> SAN (5/10/16)

4.) DFW -> SFO (5/10/16)
 
(**UPDATE (January 7th, 2016):** _Data has begun being aggregated!_)

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
$ mv env_variables_example.py env_variables.py
```
Now add your origin, destination, date for the flight, and QPX key into the creds file
( If you're unfamilar, [here](https://developers.google.com/api-client-library/python/guide/aaa_apikeys)'s how to get a Google API key!).

And finally, simply do:

```
$ python worker.py
```

and we're runnin', baby!

**Sidenote:** If you want to _query_ your data, just open another tab and do `python queryCassandra.py`. I added this for the sake of convenience so doing a SQL `SELECT` command would be as simple as a bash command.

#License
MIT
