from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collector import Node

class Graph:
    """Graph class
    draws all folders as a graph
    """
    def __init__(self,            
                 origin=(0, 0)): 
        self.origin = origin
        self.time_elapsed = 0
    
    def position(self):
        """compute the current x,y positions of the pendulum arms"""

        return (1, 1)

    def step(self, dt):
        """execute one time step of length dt and update state"""
        self.time_elapsed += dt

#------------------------------------------------------------

# set up initial state and global variables
graph = Graph()
dt = 1./30 # 30 fps

# set up figure and animation
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
energy_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)

#------------------------------------------------------------

class Visualizer:
    """ Visualizer class    
    """
    def __init__(self, root):
        self.root = root

    def run(self):


        # choose the interval based on dt and the time to animate one step
        from time import time
        t0 = time()
        self.animate(0)
        t1 = time()
        interval = 1000 * dt - (t1 - t0)

        ani = animation.FuncAnimation(fig, self.animate, frames=300,
                                      interval=interval, blit=True, init_func=self.init)

        # save the animation as an mp4.  This requires ffmpeg or mencoder to be
        # installed.  The extra_args ensure that the x264 codec is used, so that
        # the video can be embedded in html5.  You may need to adjust this for
        # your system: for more information, see
        # http://matplotlib.sourceforge.net/api/animation_api.html
        #ani.save('double_pendulum.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

        plt.show()


    def init(self):
        """initialize animation"""
        line.set_data([], [])
        time_text.set_text('')
        energy_text.set_text('')
        return line, time_text, energy_text

    def animate(self, i):
        """perform animation step"""
        global graph, dt
        graph.step(dt)

        line.set_data(*graph.position())
        time_text.set_text('time = %.1f' % graph.time_elapsed)
        return line, time_text, energy_text

