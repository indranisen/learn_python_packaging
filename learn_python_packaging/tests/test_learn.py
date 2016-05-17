from unittest import TestCase

import learn_python_packaging


class TestLearn(TestCase):

    def test_is_string(self):
        s = learn_python_packaging.learn()
        self.assertTrue(isinstance(s, basestring))
