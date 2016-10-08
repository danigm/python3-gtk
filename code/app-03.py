#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GLib

from threading import Timer


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hilos")
        self.set_default_size(500, 400)
        self.stopped = False
        self.connect("delete-event", self.quit)

        self.progressbar = Gtk.ProgressBar()
        self.progressbar.set_show_text("0%")

        self.add(self.progressbar)
        self.n = 0

        self.show_all()

    def quit(self, *args):
        self.stopped = True
        Gtk.main_quit()

    def update_progressbar(self):
        self.progressbar.set_fraction(self.n / 100)

    def time_pass(self):
        self.n += 1

        #self.update_progressbar()
        GLib.idle_add(self.update_progressbar)

        if not self.stopped and self.n < 100:
            t = Timer(0.5, self.time_pass)
            t.start()


win = MyWindow()

t = Timer(0.5, win.time_pass)
t.start()

Gtk.main()

