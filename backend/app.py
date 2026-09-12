# region IMPORTS
# Flask
from flask import Flask, jsonify, request
from flask_cors import CORS
from markupsafe import escape

# Gremlinpython
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver import serializer

# my Gremlinpython helper functions
from gremlinpython_functions import vt_dict

# Other
import json
# endregion

# region setup
# Functions
def stringify(dict):
    clean = [
        {str(k): v for k, v in item.items()}
        for item in dict
    ]
    return clean
# Connect gremlinpython to the janusgraph instance. It runs in a docker container.
connection = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g')
g = traversal().withRemote(connection)

app = Flask(__name__)
CORS(app, resources={r"/json/": {"origins": "http://localhost:5173"}})
#endregion


# Returns all vertices
@app.route('/dump/')
def serve_data():
    data = g.V().elementMap().toList()
    results = stringify(data)
    return jsonify(results)

@app.route("/v")
def hello():
    args = request.args
    results = vt_dict(args, g)
    results = stringify(results)
    return jsonify(results)
