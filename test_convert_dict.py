import unittest

from convert_dict import ConvertDict


class TestConvertDict(unittest.TestCase):
    def test_construct(self):
        o = ConvertDict({'key': 'value'})
        self.assertDictEqual({'key': 'value'}, o)

    def test_nested_dict_value(self):
        o = ConvertDict({'outer': {
            'key': 'value'
        }}, convert=False)
        self.assertIs(dict, type(o['outer']))

    def test_twice_nested_dict_value(self):
        o = ConvertDict({'outer': {
            'inner': {'key': 'value'}
        }}, convert=False)
        self.assertEqual('value', o['outer']['inner']['key'])
        self.assertIs(dict, type(o['outer']))
        self.assertIs(dict, type(o['outer']['inner']))

    def test_set_nested_dict_value_does_not_convert(self):
        o = ConvertDict()
        o['outer'] = {'key': 'value'}
        self.assertDictEqual({'outer': {'key': 'value'}}, o)
        self.assertIs(dict, type(o['outer']))

    def test_nested_dict_value_conversion(self):
        o = ConvertDict({'outer': {
            'key': 'value'
        }}, convert=True)
        self.assertIs(ConvertDict, type(o['outer']))

    def test_twice_nested_dict_value_conversion(self):
        o = ConvertDict({'outer': {
            'inner': {'key': 'value'}
        }}, convert=True)
        self.assertEqual('value', o['outer']['inner']['key'])
        self.assertIs(ConvertDict, type(o['outer']))
        self.assertIs(ConvertDict, type(o['outer']['inner']))

    def test_converted_dicts_use_child_type(self):
        class Child(ConvertDict):
            pass

        o = Child({'outer': {'inner': {'key': 'value'}}}, convert=True)
        self.assertEqual('value', o['outer']['inner']['key'])
        self.assertIs(Child, type(o['outer']))
        self.assertIs(Child, type(o['outer']['inner']))


if __name__ == '__main__':
    unittest.main()
