import unittest, os

class Example(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.branch = os.getenv("sourceBranch")

    def test_branch(self):
        self.assertEqual(self.branch, "master")