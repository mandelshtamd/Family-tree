import json
import os
from pymongo import MongoClient
import pprint
import os

from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsItem


def saveToJson(self):
    graph = {}
    graph['nodes'] = []
    for node in self.nodesMap:
        graph['nodes'].append({
            'x': str(node.x()),
            'y': str(node.y()),
            'name': node.name
        })
    with open('database.txt', 'w') as outfile:
        json.dump(graph, outfile)


def loadFromJson(self):
    if (os.stat("database.txt").st_size == 0):
        return

    with open('database.txt') as json_file:
        graph = json.load(json_file)
    for p in graph['nodes']:
        circle = QGraphicsEllipseItem(-20, -20, 40, 40)
        circle.setFlag(QGraphicsItem.ItemIsMovable)
        circle.name = p["name"]
        circle.setPos(float(p["x"]), float(p["y"]))
        circle.setToolTip(circle.name)
        self.nodesMap.append(circle)

"""
collection - trees tree - json string
function deletes all in database and insert new tree
"""
def add_to_db(db, collection, tree):
    db.collection.remove()
    collection.insert_one(tree)

"""    
collection - trees
name - name of person
"""
def get_from_db(collection):
    return collection.find_one()

"""
collection - trees
prints dictionary(json) from db
"""
def print_db(collection):
    print(get_from_db(collection))