We're going to be using [dispy](http://dispy.sourceforge.net) for distributed computing. We will be puppet masters!

# Setting up dispay on your machine

    pip install dispy

# Setting up dispy on your server

First we'll need to install Python 3 and dispy.

    apt install python3-pip
    pip3 install dispy

Then we'll need to store the external IP address into a variable that will automatically be populated every time you log in.

    echo "MY_IP=$(ifconfig  | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}')" >> ~/.bash_profile
    source ~/.bash_profile
    echo $MY_IP

# Starting dispy on your remote server from your local machine

    # Open up the SSH tunnel so the server can talk to your machine
    ssh -R 51347:localhost:51347 -i ~/.ssh/do-droplet root@REMOTE_IP_ADDRESS
    # Once you've connected, start the node server
    dispynode.py --clean -i $MY_IP

# Expand your reach

[Digital Ocean snapshot page](https://cloud.digitalocean.com/images/snapshots)

# Stopping dispy

If you get an `Address already in use` error, you can run

    ps aux | grep dispy

to find the process ID of dispy, and then `kill -9 ####` to stop the currently running dispy.