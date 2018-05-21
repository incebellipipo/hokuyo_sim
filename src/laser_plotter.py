#!/usr/bin/python2

import rospy
from sensor_msgs.msg import LaserScan
import math

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt

class Laser:
    def __init__(self):
        self.laser_data = None
        self.laser_sub = rospy.Subscriber("/hokuyo/laser/scan", LaserScan, self.laser_cb)
        
        self.fig, self.ax = plt.subplots(1, 1)         


    def laser_cb(self, msg):
        self.laser_data = msg

    def draw(self):
        if self.laser_data is None:
            return
        a = self.laser_data.angle_min
        x = []
        y = []
        for r in self.laser_data.ranges:
            # r = r if r < 3 else 3 
            x.append(math.degrees(a))
            y.append(r)
            a += self.laser_data.angle_increment
        self.ax.clear()
        self.ax.plot(x, y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.show(False)

def main():
    l = Laser()
    rospy.init_node("laser_plotter")
    while not rospy.is_shutdown():
        l.draw()

if __name__ == "__main__":
    main()
