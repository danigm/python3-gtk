#include <stdio.h>
#include <gtk/gtk.h>

#include "pycon-widget.h"

struct _PyconWidget {
    GtkBox parent;

    GtkWidget *label;
    GtkWidget *drawing;
};

struct _PyconWidgetClass {
    GtkBoxClass parent_class;
};


G_DEFINE_TYPE (PyconWidget, pycon_widget, GTK_TYPE_BOX)


static void
pycon_widget_finalize (GObject *object)
{
    PyconWidget *widget = PYCON_WIDGET (object);
    G_OBJECT_CLASS (pycon_widget_parent_class)->finalize (object);
}

static void
pycon_widget_init (PyconWidget *widget)
{
    gtk_orientable_set_orientation (GTK_ORIENTABLE (widget),
                                    GTK_ORIENTATION_VERTICAL);

    widget->drawing = gtk_image_new_from_file ("pycon.png");
    widget->label = gtk_label_new ("...");

    gtk_container_add (GTK_CONTAINER (widget), widget->drawing);
    gtk_container_add (GTK_CONTAINER (widget), widget->label);
}

static void
pycon_widget_class_init (PyconWidgetClass *klass)
{
    GObjectClass *object_class = G_OBJECT_CLASS (klass);

    object_class->finalize = pycon_widget_finalize;
}

/**
 * pycon_widget_new:
 *
 * Returns: (transfer full): the new PyconWidget created
 */
GtkWidget *
pycon_widget_new (void)
{
    return g_object_new (PYCON_TYPE_WIDGET, NULL);
}

/**
 * pycon_widget_set_text:
 * @widget: a #PyconWidget
 * @text: the text to set
 *
 * Sets the text to the widget.
 */
void
pycon_widget_set_text (PyconWidget *widget,
                       gchar    *text)
{
    gtk_label_set_text (GTK_LABEL (widget->label), text);
}
