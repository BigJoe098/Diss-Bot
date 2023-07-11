# Diss-Bot
A discord bot that does a lot of things for any server. Including stickers, admin roles, and so much more. 

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/BigJoe098/Diss-Bot
    $ cd {{ Path to directory with the project }}

Follow along as your requirments as below.

### Virtualenv

If you want to install the virtualenv then you will need to first create the virtual enviroment then follow along with the steps in no
virtual enviroment

FOR LINUX/MAC:
  
    $ sudo apt-get install python3.6-venv
    $ python3 -m venv env
    $ source env/bin/activate
  
  
FOR WINDOWS:
  
    $ py -m pip install --user virtualenv
    $ py -m venv env
    $ .\env\Scripts\activate


### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages. Note the api token needs to be pasted in a variable named TOKEN in main.py.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip install -r requirements.txt
    
And then follow the steps as in the tutorial below:

    https://builtin.com/software-engineering-perspectives/discord-bot-python

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install the requirements by running,
Note the api token needs to be pasted in a variable named TOKEN in main.py

    $ pip install -r requirements.txt
    
And then follow the steps as in the tutorial below:

    https://builtin.com/software-engineering-perspectives/discord-bot-python
