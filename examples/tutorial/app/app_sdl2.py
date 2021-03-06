#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This example shows how to actively select and test the pyglet backend.

You should see a black window and any mouse or keyboard event should be
detected. A timer is also run every second and it should print "tick !"
every second.
"""

from vispy import app, use, gloo
use('sdl2')


class Canvas(app.Canvas):

    def __init__(self, *args, **kwargs):
        app.Canvas.__init__(self, *args, **kwargs)
        timer = app.Timer(1.0)
        timer.connect(self.on_timer)
        timer.start()

    def on_initialize(self, event):
        gloo.set_clear_color('black')
        print('on_initialize')

    def on_close(self, event):
        print('on_close')

    def on_resize(self, event):
        print('on_resize (%dx%d)' % event.size)

    def on_key_press(self, event):
        print('on_key_press: %s' % event.text)

    def on_key_release(self, event):
        print('on_key_release')

    def on_mouse_press(self, event):
        print('on_mouse_press: %d' % event.button)

    def on_mouse_release(self, event):
        print('on_mouse_release')
        print(event.trail())

    def on_mouse_move(self, event):
        print('on_mouse_move (%dx%d)' % event.pos)

    def on_mouse_wheel(self, event):
        print('on_mouse_wheel: %r' % (event.delta,))

    def on_draw(self, event):
        print('on_draw')
        gloo.clear(color=True, depth=True)

    def on_timer(self, event):
        print('tick !')

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    canvas = Canvas(close_keys='escape')
    canvas.show()
    app.run()
