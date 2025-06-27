import unittest

from myqtile.tests.widget_factory_test import WidgetFactoryTest


def run_suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetFactoryTest("test_init"))
    suite.addTest(WidgetFactoryTest("test_generate_list"))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(run_suite())
