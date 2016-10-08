#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ventana")
        self.set_default_size(500, 400)
        self.connect("delete-event", Gtk.main_quit)

        self.label = Gtk.Label('¡Hola Mundo!')
        self.add(self.label)

        self.show_all()


win = MyWindow()
Gtk.main()
