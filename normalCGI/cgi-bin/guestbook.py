#!/usr/bin/env python
#coding: utf-8

import shelve

from flask import Flask , request, render_template, redirect, escape, Markup

application = Flask(__name__)

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    """Save the comment data
    """

    #open the shelve moduel database File

    database = shelve.open(DATA_FILE)

    if 'greeting_list' not in database:
        greeting_list=[]
    else:
        #get the greeting_list from databass
        greeting_list=database['greeting_list']

    greeting_list.insert(0, {
        'name':name,
        'comment':comment,
        'create_at':create_at,
    })

    #update the database
    database['greeting_list']=greeting_list

    #close the database file
    database.close()

def load_data():
    """Return the comment data saved before
    """

    #open the shelve module database file
    database = shelve.open(DATA_FILE)

    #get the greeting_list if not , just return empty list.
    greeting_list = database.get('greeting_list', [])

    database.close()

    return greeting_list

@application.route('/')
def index():
    """Top patge
    Use Template to show page
    """
    #use the comment data
    greeting_list = load_data()

    return render_template('index.html', greeting_list = greeting_list)

if __name__=='__main__':
    #Run  the application when the IP address is 127.0.0.1 and the port is 5000
    application.run('127.0.0.1', 5000, debug=True)

