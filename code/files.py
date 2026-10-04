# file to set up the .pkl files

import pickle

#settings = []

#save the variable to a .pkl file
def save(data, fileName):
    pickle.dump(data, open(f"resources/{fileName}.pkl", "wb"))

#load a variable from a .pkl file
def load(fileName):
    fileName = pickle.load(open(f"resources/{fileName}.pkl", "rb"))
    return fileName

#save(settings, "settings")