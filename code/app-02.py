#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ventana")
        self.set_default_size(500, 400)
        self.connect("delete-event", Gtk.main_quit)

        self.button = Gtk.Button('Pulsa aquí')
        self.button.connect('clicked', self.button_clicked)

        self.add(self.button)
        self.n = 0

        #self.button.emit('clicked')

        self.show_all()

    def button_clicked(self, button):
        self.n += 1
        self.button.set_label("pulsado {}".format(self.n))


win = MyWindow()
Gtk.main()

