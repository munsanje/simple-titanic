#Simple Data Analysis on Titanic Data Set

**This program requires you to perform three simple steps:**

1. Clone this repo
2. Setting up the webserver
3. Opening the webpage

**1. Clone this repo**

Follow the instructions on Github to clone this repo to your local machine. Once you have done that, open up a terminal and navigate to the repository.

**2. Setting up the webserver**

This guide assumes you have `python3`, `python3-pip` and `virtualenv` installed. If not, simply run:

    simple-titanic$ sudo apt-get install python3 python3-pip virtualenv

Now create and enter a virtual environment by running:

    simple-titanic$ virtualenv ve
    simple-titanic$ source ve/bin/activate

Install the package requirements:

    (ve)simple-titanic$ pip3 install -r requirements.txt

Finally, start the server:

    (ve)simple-titanic$ python3 server.py

**3. Opening the webpage**

Now that the server has been started, simply open up your favorite browser and enter the url `127.0.0.1:5000`
