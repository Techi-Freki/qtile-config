from qtile_extras.widget.decorations import PowerLineDecoration


class MyDecorations(object):

    @staticmethod
    def get_decorations() -> dict:
        return { "decorations": [ PowerLineDecoration() ] }
