import unittest

from attribute_dict import AttributeDict


# noinspection PyUnresolvedReferences
class TestAttributeDict(unittest.TestCase):
    def test_get_key(self):
        o = AttributeDict({'key': 'value'})
        self.assertEqual('value', o.key)

    def test_set_key(self):
        o = AttributeDict()
        self.assertDictEqual({}, o)
        o.key = 'value'
        self.assertEqual('value', o.key)

    def test_get_nested_dict_value(self):
        o = AttributeDict({'outer': {
            'inner': 'value'
        }})
        self.assertEqual('value', o.outer['inner'])

    def test_get_nested_dict_value_convert_inner_dict(self):
        o = AttributeDict({'outer': {
            'key': 'value'
        }}, convert_dict=True)
        self.assertIs(AttributeDict, type(o.outer))
        self.assertEqual('value', o.outer.key)

    def test_set_nested_dict_value_does_not_convert(self):
        o = AttributeDict()
        o.outer = {'key': 'value'}
        self.assertIs(dict, type(o.outer))
        self.assertEqual('value', o.outer['key'])


if __name__ == '__main__':
    unittest.main()
