# Gremlinpython
from gremlin_python.process.graph_traversal import __
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.traversal import T


'''
The argument 'g' is the graph. In the file where the function is used, a connection to the JanusGraph server has to be established using:
connection = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g')
g = traversal().withRemote(connection)

v: Vertex
e: edge
t: traversal
'''

def vt_dict(dict, g):
    traversal = g.V()
    for k, v in dict.items():
        if k == "label":
            traversal = traversal.has(T.label, v)
        elif k == "id":
            traversal = traversal.has(T.id, v)
        else:
            traversal = traversal.has(k, v)
    results = traversal.elementMap().toList()
    return results




def main():
  print('hi')

if __name__ == '__main__':
  main()