import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Pycon', '0.1')
from gi.repository import Pycon

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Pycon")

        self.pycon = Pycon.Widget()
        #self.pycon.set_text("HOLA")
        self.add(self.pycon)

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
