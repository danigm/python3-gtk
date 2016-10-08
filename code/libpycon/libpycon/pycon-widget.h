#ifndef __PYCON_WIDGET_H__
#define __PYCON_WIDGET_H__

#include <gtk/gtk.h>
#include <glib-object.h>
#include <glib.h>

G_BEGIN_DECLS

#define PYCON_TYPE_WIDGET           (pycon_widget_get_type ())
#define PYCON_WIDGET(obj)           (G_TYPE_CHECK_INSTANCE_CAST (obj, PYCON_TYPE_WIDGET, PyconWidget))
#define PYCON_WIDGET_CLASS(cls)     (G_TYPE_CHECK_CLASS_CAST (cls, PYCON_TYPE_WIDGET, PyconWidgetClass))
#define PYCON_IS_WIDGET(obj)        (G_TYPE_CHECK_INSTANCE_TYPE (obj, PYCON_TYPE_WIDGET))
#define PYCON_IS_WIDGET_CLASS(obj)  (G_TYPE_CHECK_CLASS_TYPE (obj, PYCON_TYPE_WIDGET))
#define PYCON_WIDGET_GET_CLASS(obj) (G_TYPE_INSTANCE_GET_CLASS ((obj), PYCON_TYPE_WIDGET, PyconWidgetClass))

typedef struct _PyconWidget      PyconWidget;
typedef struct _PyconWidgetClass PyconWidgetClass;

GType             pycon_widget_get_type                        (void) G_GNUC_CONST;

GtkWidget        *pycon_widget_new                             (void);

//void              pycon_widget_set_text                        (PyconWidget *widget,
//                                                                gchar       *text);

G_END_DECLS

#endif /* __PYCON_WIDGET_H__ */

