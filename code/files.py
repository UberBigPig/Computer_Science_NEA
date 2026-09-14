# file to set up the .pkl files

import pickle

#accountLogin = []

#save the variable to a .pkl file
def save(file, fileName):
    pickle.dump(file, open(f"resources/{fileName}.pkl", "wb"))

#load a variable from a .pkl file
def load(fileName):
    fileName = pickle.load(open(f"resources/{fileName}.pkl", "rb"))
    return fileName

#save(accountLogin, "accountLogin")