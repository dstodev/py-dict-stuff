import unittest

from attribute_dict import AttributeDict


# noinspection PyUnresolvedReferences
class TestAttributeDict(unittest.TestCase):
    def test_set_key(self):
        o = AttributeDict()
        self.assertEqual({}, o.key)
        o.key = 'value'
        self.assertEqual('value', o.key)

    def test_get_key(self):
        o = AttributeDict({'key': 'value'})
        self.assertEqual('value', o.key)

    def test_get_nested_dict_value(self):
        o = AttributeDict({'outer': {
            'inner': 'value'
        }})
        self.assertEqual('value', o.outer.inner)

    def test_set_nested_dict_value(self):
        o = AttributeDict()
        o.outer = {'inner': 'value'}
        self.assertEqual('value', o.outer.inner)

    def test_set_nested_attribute_dict_init(self):
        o = AttributeDict({'outer': {
            'inner': {}
        }})
        o.outer.inner.key = 'value'
        self.assertEqual('value', o.outer.inner.key)

    def test_set_nested_attribute_dict_adhoc(self):
        o = AttributeDict()
        o.outer.inner.key = 'value'
        self.assertEqual('value', o.outer.inner.key)

    def test_converted_nested_type(self):
        o = AttributeDict({'outer': {
            'inner': {}
        }})
        self.assertIs(AttributeDict, type(o.inner))

    def test_converted_adhoc_type(self):
        o = AttributeDict()
        o.outer.key = 'value'
        self.assertIs(AttributeDict, type(o.outer))

    def test_converted_dict_type(self):
        o = AttributeDict()
        o.outer = {}
        self.assertIs(AttributeDict, type(o.outer))

    def test_conversion_with_setitem(self):
        o = AttributeDict()
        o['outer'] = {}
        self.assertIs(AttributeDict, type(o.outer))

    def test_conversion_type_uses_child_type(self):
        class Child(AttributeDict):
            pass

        o = Child()
        o.outer = {}
        self.assertIs(Child, type(o.outer))


if __name__ == '__main__':
    unittest.main()
