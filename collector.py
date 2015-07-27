import datetime
import pickle

class Node:
    """Contains history about one folder/file"""
    def __init__(self, path):
        self.path = path
        self.childs = []
        self.log = []

    def pickle(self):
        f = open('test_file', 'wb')
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        f.close()

    @staticmethod
    def unpickle():
        with open('test_file', 'rb') as f:
            return pickle.load(f)

root = Node("C:/")
root.log.append((datetime.datetime(2015, 7, 21, 16, 25), 'ivan'))

n1 = Node("C:/2")
root.childs.append(n1)

#root.pickle()

# test
#data = Node.unpickle()
#print(data.path)
