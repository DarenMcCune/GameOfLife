from flask import Flask, request
from flask_restful import abort, Resource, Api
from algorithm import Game

app=Flask(__name__)
api=Api(app)
boards={}


def abort_if_no_such_session(session_id):
    if(session_id not in boards.keys()):
        abort(404, message="No such session with id %s" % session_id)

@api.resource('/UpdateCell', resource_class_args={'board_dict': boards})
class UpdateCell(Resource):
    def __init__(self, board_dict):
        self.board_dict=board_dict
    #TODO Handle user click on cell
    pass

@api.resource('/GetBoard/<session_id>', resource_class_args={'board_dict': boards})
class GetBoard(Resource):
    def __init__(self, board_dict):
        self.board_dict=board_dict

    def get(self, session_id):
        abort_if_no_such_session(session_id)
        return self.board_dict[boards]._get_physical_board().flatten()


@api.resource('/Tick', resource_class_args={'board_dict': boards})
class Tick(Resource):
    def __init__(self, board_dict):
        self.board_dict=board_dict
    #TODO Handle play_pause_events
    pass



@api.resource('/CreateBoard', resource_class_args={'board_dict': boards})
class CreateBoard(Resource):
    def __init__(self, board_dict):
        self.board_dict=board_dict

    def put(self, session_id):
        self.board_dict[session_id] = Game()

if __name__=='__main__':
    boards['0'] = Game(5, 5)
    boards['0'].flip_physical_board_cell(2)
    boards['0'].flip_physical_board_cell(7)
    boards['0'].flip_physical_board_cell(12)
    app.run(debug=True)