from flask import Flask, request
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

class updateCell:
    #TODO Handle user click on cell
    pass

class getBoard:
    #TODO Get info about the current board state
    pass

class play_pause:
    #TODO Handle play_pause_events
    pass
