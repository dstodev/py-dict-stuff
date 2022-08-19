import unittest

from observable_attribute_dict import ObservableAttributeDict


class TestObservableAttributeDict(unittest.TestCase):
    def test_construct(self):
        o = ObservableAttributeDict()

    def test_notify(self):
        updates = []
        o = ObservableAttributeDict()
        o.observers.append(updates.append)
        self.assertEqual([], updates)
        o.key = 'value'
        self.assertEqual([o.Update(o, 'key', None, 'value')], updates)

    def test_pre_notify(self):
        updates = []
        o = ObservableAttributeDict({'key': 'value'}, observers=[updates.append], pre_notify=True)
        self.assertEqual([o.Update(o, 'key', None, 'value')], updates)

    def test_converted_type(self):
        o = ObservableAttributeDict({'outer': {
            'inner': 'key'
        }})
        self.assertIs(ObservableAttributeDict, type(o.inner))


if __name__ == '__main__':
    unittest.main()
