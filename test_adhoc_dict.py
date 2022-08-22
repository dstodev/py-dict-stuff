import unittest

from adhoc_dict import AdhocDict


class TestAdhocDict(unittest.TestCase):
    def test_set_adhoc_key(self):
        o = AdhocDict()
        self.assertDictEqual({}, o)
        o['outer']['key'] = 'value'
        self.assertDictEqual({'outer': {'key': 'value'}}, o)
        self.assertIs(AdhocDict, type(o['outer']))

    def test_adhoc_dicts_use_child_type(self):
        class Child(AdhocDict):
            pass

        o = Child()
        o['outer']['key'] = 'value'
        self.assertIs(Child, type(o['outer']))


if __name__ == '__main__':
    unittest.main()
