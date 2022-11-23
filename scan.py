import pandas as pd
import numpy as np
import time
import os

class scan:
    def __init__(self, id, nature, path):
        self.id = id
        self.nature = nature
        self.path = path

    def __str__(self):
        # repr as dict 
        return f"{{'id': {self.id}, 'nature': {self.nature}, 'path': {self.path}}}"
    
    def exists(self):
        return os.path.exists(self.path)
    
    @staticmethod
    def from_file(file):
        # read from file
        my_list = []
        scans = pd.read_csv(file)
        for s in scans.to_dict('records'):
            my_list.append(scan(s['id'], s['nature'], s['path']))
        return my_list