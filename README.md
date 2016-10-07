#Simple Data Analysis on Titanic Data Set

**This program requires you to perform two steps:**

1. Setting up the webserver
2. Opening the webpage

**1. Setting up the webserver**

This guide assumes you have `python3`, `python3-pip` and `virtualenv` installed. If not, simply run:

    $ sudo apt-get install python3 python3-pip virtualenv

Now create and enter a virtual environment by running:

    $ virtualenv ve
    $ source ve/bin/activate

Install the package requirements:

    (ve)$ pip3 install -r requirements.txt

Finally, start the server:

    (ve)$ python3 server.py

**2. Opening the webpage**

Now that the server has been started, simply open up your favorite browser and enter the url `127.0.0.1:5000`
