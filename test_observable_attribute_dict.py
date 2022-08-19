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


if __name__ == '__main__':
    unittest.main()
