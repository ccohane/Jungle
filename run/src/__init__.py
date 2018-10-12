#!/usr/bin/env python3

# this will be an app with Mongo DB

from flask import Flask
import os
import datetime
import json

app = Flask(__name__)

from src.controllers import routes


# Define a function named keymaker
def keymaker(supercontroller, filename='secret_key'):
    pathname = os.path.join(supercontroller.instance_path, filename)
    try:
        supercontroller.secret_key = open(pathname, 'rb').read()
    except IOError:
        path_to_parent_directory = os.path.dirname(pathname)
        if not os.path.isdir(path_to_parent_directory):
            os.system('mkdir -p {pathname}'.format(pathname=path_to_parent_directory))
        os.system('cowsay -d "I AM 0xdeadbeef"')
        os.system('head -c 24 /dev/urandom > {filename}'.format(filename=pathname))
        supercontroller.secret_key = open(pathname, 'rb').read()

keymaker(app)

