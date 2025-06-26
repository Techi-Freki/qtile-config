import sys
import inspect

from qtile_extras import widget


class WidgetFactory(object):
    @staticmethod
    def init(type: str, font: str, fontsize: int, padding: int, **attr):
        return WidgetFactory._init(type, font, fontsize, padding, **attr)

    @staticmethod
    def generate_list() -> list:
        widgets = []
        for name, obj in inspect.getmembers(sys.modules[widget.__name__]):
            if inspect.isclass(obj):
                widgets.append({ "name": name, "obj": obj })
        return widgets

    @staticmethod
    def _init(type: str, font: str, fontsize: int, padding: int, **attr):
        widgets = WidgetFactory.generate_list()
        requested_widget = next((item for item in widgets if item["name"] == type))
        return requested_widget["obj"](font=font, fontsize=fontsize, padding=padding, **attr)
