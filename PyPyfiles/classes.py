from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event


class randgen:
    def __init__(self):
        """
        Generate a random number every 2 seconds and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        print("Making random numbers")
        while not thread_stop_event.isSet():
            number = 69
            print(number)
            socketio.emit('newnumber', {'number': number}, namespace='/test')
            socketio.sleep(1)