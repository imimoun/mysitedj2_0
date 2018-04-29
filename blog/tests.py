from django.test import TestCase


class BlogTestCase(TestCase):
    def test_001_wrong_test(self):
        self.fail("Hello world!")
