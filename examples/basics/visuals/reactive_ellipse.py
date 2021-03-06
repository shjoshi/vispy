# -*- coding: utf-8 -*-
# Copyright (c) 2014, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

"""
Simple demonstration of reactive EllipseVisual. 
"""

import vispy.app
from vispy import gloo
from vispy.scene import visuals


class Canvas(vispy.app.Canvas):
    def __init__(self):
        self.ellipse = visuals.Ellipse(pos=(0.0, 0.0, 0), radius=[0.4, 0.3],
                                       color=(1, 0, 0, 1),
                                       border_color=(1, 1, 1, 1),
                                       start_angle=180., span_angle=150.)
        
        vispy.app.Canvas.__init__(self, close_keys='escape')
        self.size = (800, 800)
        self.show()
        
        self.timer = vispy.app.Timer(1.0 / 60)  # change rendering speed here
        self.timer.connect(self.on_timer)
        self.timer.start()

    def on_timer(self, event):
        self.ellipse.radius[0] += 0.001
        self.ellipse.radius[1] += 0.0015
        self.ellipse.span_angle += 0.6
        self.update()

    def on_mouse_press(self, event):
        self.ellipse.radius = [0.4, 0.3]
        self.ellipse.span_angle = 150.
        self.update()

    def on_draw(self, ev):
        gloo.clear(color='black')
        gloo.set_viewport(0, 0, *self.size)
        self.ellipse.draw()
        

if __name__ == '__main__':
    win = Canvas() 
    import sys
    if sys.flags.interactive != 1:
        vispy.app.run()
