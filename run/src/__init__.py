#!/usr/bin/env python3

# this will be an app with Mongo DB

from flask import Flask
import os
import datetime
import json

app = Flask(__name__)

from src.controllers import routes



