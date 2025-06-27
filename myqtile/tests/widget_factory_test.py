import unittest

from myqtile.factories import WidgetFactory


class WidgetFactoryTest(unittest.TestCase):
    def test_init(self):
        text_box = WidgetFactory.init('TextBox', 'sans', 12, 5)
        print(text_box)
        self.assertIsNotNone(text_box)

    def test_generate_list(self):
        widgets = WidgetFactory.generate_list()
        self.assertIsNotNone(widgets)
        self.assertGreater(len(widgets), 0)
