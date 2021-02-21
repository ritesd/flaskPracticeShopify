import requests
import MySQLdb
import json


class Queries:
    def __init__(self):
        pass

    def connect_db(self):
        self.db = MySQLdb.connect(
            host="localhost", user="root", passwd="PASSWORD", db="mishipay"
        )
        self.cursor = self.db.cursor()

    def query(self, query, type=None):
        self.cursor.execute(query)
        if type == "SELECT":
            return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.db.commit()
        self.db.close()
