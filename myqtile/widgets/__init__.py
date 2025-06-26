from myqtile.defaults import widget_defaults
from myqtile.factories import WidgetFactory


class MyWidget(object):
    def __init__(self, type: str, **attr):
        self.type = type
        self.font = widget_defaults["font"]
        self.fontsize = widget_defaults["fontsize"]
        self.padding = widget_defaults["padding"]
        self.attributes = attr
        self.widget = WidgetFactory.init(self.type,
                            self.font,
                            self.fontsize,
                            self.padding,
                            **self.attributes)
