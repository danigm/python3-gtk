AC_PREREQ(2.60)
AC_INIT([libpycon],[0.1],[danigm@wadobo.com])
AC_CONFIG_AUX_DIR([build])
AM_INIT_AUTOMAKE([1.10 -Wall -Werror dist-bzip2])
AM_SILENT_RULES([yes])

GNOME_COMMON_INIT

# automake 1.12 seems to require this, but automake 1.11 doesn't recognize it
m4_pattern_allow([AM_PROG_AR])
AM_PROG_AR

AC_PROG_CC
# Compiling sources with per-target flags requires AM_PROG_CC_C_O
AM_PROG_CC_C_O
AC_PROG_INSTALL
AC_PROG_LIBTOOL

PKG_CHECK_MODULES(PYCON,
                  gtk+-3.0)

AC_SUBST(PYCON_CFLAGS)
AC_SUBST(PYCON_LIBS)

AC_CONFIG_FILES([
    Makefile
    libpycon.pc
    libpycon/Makefile
])

# introspection
GOBJECT_INTROSPECTION_CHECK([1.30.0])

AC_OUTPUT
