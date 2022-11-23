import pandas as pd
import numpy as np
import time


class user:
    ids = 0
    def __init__(self, nom, prenom, poids, taille, id=None):
        self.nom = nom
        self.prenom = prenom
        self.poids = poids
        self.taille = taille
        if id is None:
            self.id = user.ids
            user.ids += 1
        elif id >= user.ids:
            self.id = id
            user.ids = id + 1
    
    def __str__(self):
        # repr as dict 
        return f"{{'nom': {self.nom}, 'prenom': {self.prenom}, 'poids': {self.poids}, 'taille': {self.taille}, 'id': {self.id}}}"
    
    @staticmethod
    def from_file(file):
        # read from file
        my_list = []
        users = pd.read_csv(file)
        for u in users.to_dict('records'):
            my_list.append(user(u['nom'], u['prenom'], u['poids'], u['taille'], u['id']))
        return my_list
    