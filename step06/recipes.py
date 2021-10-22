import flask

api = flask.Flask(__name__)
api.config['DEBUG'] = True

@api.route('/', methods=['GET'])
def test():
    return '<h1>Hello</h1>'


api.run()