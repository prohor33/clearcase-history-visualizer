import collector
from collector import Node
from visualizer import Visualizer

root = Node.unpickle()
print(root.childs[0].path)

visu = Visualizer(root)
visu.run()
