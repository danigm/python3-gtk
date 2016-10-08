const Pycon = imports.gi.Pycon;
const Gtk = imports.gi.Gtk;

Gtk.init(null);
let win = new Gtk.Window({type: Gtk.WindowType.TOPLEVEL});
let pycon = new Pycon.Widget();

win.add(pycon);
win.show_all();

win.connect("delete-event", Gtk.main_quit);
win.set_title("Pycon js");

//pycon.set_text("HOLA");

Gtk.main();
