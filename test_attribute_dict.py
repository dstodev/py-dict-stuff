import unittest

from attribute_dict import AttributeDict


# noinspection PyUnresolvedReferences
class TestAttributeDict(unittest.TestCase):
    def test_get_key(self):
        o = AttributeDict({'key': 'value'})
        self.assertDictEqual({'key': 'value'}, o)
        self.assertEqual('value', o.key)

    def test_set_key(self):
        o = AttributeDict()
        self.assertDictEqual({}, o)
        o.key = 'value'
        self.assertEqual('value', o.key)

    def test_nested_dict_value(self):
        o = AttributeDict({'outer': {
            'key': 'value'
        }})
        self.assertEqual('value', o.outer['key'])
        self.assertIs(dict, type(o.outer))

    def test_nested_dict_value_conversion(self):
        o = AttributeDict({'outer': {
            'key': 'value'
        }}, convert_dict=True)
        self.assertEqual('value', o.outer.key)
        self.assertIs(AttributeDict, type(o.outer))

    def test_twice_nested_dict_value_conversion(self):
        o = AttributeDict({'outer': {
            'inner': {'key': 'value'}
        }}, convert_dict=True)
        self.assertEqual('value', o.outer.inner.key)
        self.assertIs(AttributeDict, type(o.outer))
        self.assertIs(AttributeDict, type(o.outer.inner))

    def test_set_nested_dict_value_does_not_convert(self):
        o = AttributeDict()
        o.outer = {'key': 'value'}
        self.assertDictEqual({'outer': {'key': 'value'}}, o)
        self.assertIs(dict, type(o.outer))


if __name__ == '__main__':
    unittest.main()
