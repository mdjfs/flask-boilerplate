
from flask import Flask

class Server(Flask):
    """ Custom class for flask object """

    def __init__(self, **kwargs):
        super().__init__(__name__, **kwargs)