# ------------------------------------------------- #
# Title: Assingment 07
# Description: A simple example of storing data in a binary file
# ChangeLog: (Nick Soldano, 11/27/2021, File Created)
# <Nick Soldano>,<11.27.2021>,Created Script
# ------------------------------------------------- #
# This is an example of a pickling program

# Data -------------------------------------------- #

import pickle
list1 = ['cat', 'dog', 1, 10, 'mouse']


def save_pickle(file_to_pickle):
    file_handle = open('list_obj.pkl', 'wb')
    pickle.dump(list1, file_handle)

save_pickle(list1)

list_obj = 'list_obj.pkl'

def open_pickle(pickle_to_open):
    list_file = open('list_obj.pkl', 'rb')
    list2 = pickle.load(list_file)
    print(list2)

open_pickle(list_obj)