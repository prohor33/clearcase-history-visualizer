#from collector import *
from collector import Node
from visualizer import Visualizer

root = Node.unpickle()
print ("childs = ", len(root.childs))
print(root.childs[0].path)

visu = Visualizer(root)
visu.run()
