# python3-gtk

Este repositorio contiene la presentación de python3-gtk para la pycones
2016.

Para la presentación se usa pinpoint:

 * https://wiki.gnome.org/Apps/Pinpoint

Todo el código está dentro de /code, con scripts ejecutables sencillos. El
código dentro de libpycon muestra un ejemplo de código Gtk en C, con
anotaciones gir, que generan el binding automático a python con tan sólo
compilar e instalar en sistema.

## Compilar libpycon

```
$ ./autogen.sh
$ ./configure --prefix=/usr
$ make
$ sudo make install
```

Tras la instalación el módulo se pueden usar los ejemplos de código app.py
y app.js que hacen uso directamente del widget que provee libpycon, con los
bindings automáticos que provee gir.

Se puede ver el fichero xml que se usa para el binding de gir en:
* /usr/share/gir-1.0/Pycon-0.1.gir
