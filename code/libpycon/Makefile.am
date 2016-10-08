SUBDIRS = libpycon

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = libpycon.pc

# introspection
DISTCHECK_CONFIGURE_FLAGS = --enable-introspection

EXTRA_DIST = \
	$(pkgconfig_DATA).in

DISTCLEANFILES = \
	$(pkgconfig_DATA)
