#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GLib



class Handler:
    def __init__(self, builder):
        self.builder = builder
        self.n = 0

    def on_window_delete_event(self, *args):
        Gtk.main_quit(*args)

    def on_button_clicked(self, button):
        self.n += 1

        button = self.builder.get_object("button")
        label = self.builder.get_object("label")
        progressbar = self.builder.get_object("progressbar")

        progressbar.set_fraction(self.n / 100)
        label.set_text("pulsado {} veces".format(self.n))


builder = Gtk.Builder()
builder.add_from_file("example.glade")
builder.connect_signals(Handler(builder))

window = builder.get_object("window")
window.show_all()

Gtk.main()
