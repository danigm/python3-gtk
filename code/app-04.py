#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GLib


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Layout 1")
        self.set_default_size(500, 400)
        self.stopped = False
        self.connect("delete-event", self.quit)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.img = Gtk.Image.new_from_file("pycon-small.png")
        self.label = Gtk.Label("texto")
        self.button = Gtk.Button("click")
        self.progressbar = Gtk.ProgressBar()
        self.progressbar.set_show_text("0%")

        self.button.connect('clicked', self.callback)

        self.box2.pack_start(self.label, True, True, 0)
        self.box2.add(self.img)

        self.box.pack_start(self.box2, True, True, 0)
        self.box.add(self.progressbar)
        self.box.add(self.button)

        self.add(self.box)
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

