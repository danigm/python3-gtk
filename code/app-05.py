#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GLib


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Layout 2")
        self.set_default_size(500, 400)
        self.stopped = False
        self.connect("delete-event", self.quit)

        self.grid = Gtk.Grid()

        self.img = Gtk.Image.new_from_file("pycon-small.png")
        self.label = Gtk.Label("texto")
        self.button = Gtk.Button("click")
        self.progressbar = Gtk.ProgressBar()
        self.progressbar.set_show_text("0%")

        self.button.connect('clicked', self.callback)

        self.grid.set_column_homogeneous(True)
        # left, top, with, height
        self.grid.attach(self.label, 0, 0, 1, 1)
        self.grid.attach(self.img, 1, 0, 1, 1)
        self.grid.attach(self.progressbar, 0, 1, 2, 1)
        self.grid.attach(self.button, 0, 2, 2, 1)

        self.add(self.grid)
        self.n = 0

        self.show_all()

    def quit(self, *args):
        self.stopped = True
        Gtk.main_quit()

    def callback(self, button):
        self.n += 1
        self.progressbar.set_fraction(self.n / 100)
        self.label.set_text("pulsado {} veces".format(self.n))

win = MyWindow()
Gtk.main()

