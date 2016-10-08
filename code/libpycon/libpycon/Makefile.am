lib_LTLIBRARIES = libpycon.la

INST_H_FILES = \
	pycon-widget.h

libpyconincludedir = $(includedir)/libpycon
libpyconinclude_HEADERS = $(INST_H_FILES)

libpycon_la_SOURCES = \
	pycon-widget.c			\
	$(INST_H_FILES)

libpycon_la_CPPFLAGS = \
	-I$(top_builddir)	\
	-I$(srcdir)			\
	-I$(top_srcdir)		\
	$(AM_CPPFLAGS)

libpycon_la_CFLAGS = \
	$(PYCON_CFLAGS)	\
	$(WARN_CFLAGS)	\
	$(AM_CFLAGS)

libpycon_la_LDFLAGS = \
	-no-undefined						\
	-export-symbols-regex "^pycon_*"	\
	$(AM_LDFLAGS)

libpycon_la_LIBADD = \
	$(PYCON_LIBS)

-include $(INTROSPECTION_MAKEFILE)
INTROSPECTION_GIRS =
INTROSPECTION_SCANNER_ARGS = --add-include-path=$(srcdir)
INTROSPECTION_COMPILER_ARGS = --includedir=$(srcdir)

if HAVE_INTROSPECTION
introspection_sources = $(libpycon_la_SOURCES)

Pycon-0.1.gir: libpycon.la
Pycon_0_1_gir_INCLUDES = Gtk-3.0
Pycon_0_1_gir_CFLAGS = $(INCLUDES)
Pycon_0_1_gir_LIBS = libpycon.la
Pycon_0_1_gir_FILES = $(introspection_sources)
Pycon_0_1_gir_SCANNERFLAGS = --warn-all
INTROSPECTION_GIRS += Pycon-0.1.gir

girdir = $(datadir)/gir-1.0
gir_DATA = $(INTROSPECTION_GIRS)

typelibdir = $(libdir)/girepository-1.0
typelib_DATA = $(INTROSPECTION_GIRS:.gir=.typelib)

CLEANFILES = $(gir_DATA) $(typelib_DATA)
endif
