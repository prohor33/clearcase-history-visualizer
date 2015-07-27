from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collector import Node
from matplotlib import collections  as mc
import math

class Graph:
    """Graph class
    draws all folders as a graph
    """
    def __init__(self,
                 root,
                 origin=(5, 5)): 
        self.origin = origin
        self.time_elapsed = 0
        self.root = root
        self.set_graph_points(root)
    
    def get_lines(self):
        # test
        lines, c = self.get_graph_lines()
        
        #lines.append()
        #lines = [[(0, 1), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)]]
        #c = np.array([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])

        lc = mc.LineCollection(lines, colors=c, linewidths=2)

        return lc

    def step(self, dt):
        """execute one time step of length dt and update state"""
        self.time_elapsed += dt

    def set_graph_points(self, root):
        self.traverse_and_set_points(root, self.origin, 2.0)

    def traverse_and_set_points(self, node, pos, radius):
        node.pos = pos
        angle = 0
        if len(node.childs) is 0:
            return
        delta_angle = 2 * math.pi / len(node.childs)
        for child in node.childs:
            next_pos = (pos[0] + math.sin(angle), pos[1] + math.cos(angle))
            print("angle = ", angle)
            print("math.sin(angle) = ", math.sin(angle))
            self.traverse_and_set_points(child, next_pos, radius * 0.8)
            angle = angle + delta_angle

    def get_graph_lines(self):
        lines = []
        c = []
        self.traverse_and_get_lines(self.root, lines, c)
        return lines, c

    def traverse_and_get_lines(self, node, lines, c):
        for child in node.childs:
            lines.append((node.pos, child.pos))
            c.append((1, 0, 0, 1))
            self.traverse_and_get_lines(child, lines, c)
        
#------------------------------------------------------------

# set up initial state and global variables
dt = 1./30 # 30 fps

# set up figure and animation
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(0, 10), ylim=(0, 10))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
energy_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)

#------------------------------------------------------------

class Visualizer:
    """ Visualizer class    
    """
    def __init__(self, root):
        self.graph = Graph(root)

    def run(self):


        # choose the interval based on dt and the time to animate one step
        from time import time
        t0 = time()
        self.animate(0)
        t1 = time()
        interval = 1000 * dt - (t1 - t0)

        ani = animation.FuncAnimation(fig, self.animate, frames=300,
                                      interval=interval, blit=True, init_func=self.init)

        plt.show()


    def init(self):
        """initialize animation"""
        line.set_data([], [])
        time_text.set_text('')
        energy_text.set_text('')
        return line, time_text, energy_text

    def animate(self, i):
        """perform animation step"""
        global dt
        self.graph.step(dt)

        # TODO: change dynamic, not add?
        ax.add_collection(self.graph.get_lines())
        time_text.set_text('time = %.1f' % self.graph.time_elapsed)
        return line, time_text, energy_text

