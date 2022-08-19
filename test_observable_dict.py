import unittest

from observable_dict import ObservableDict


class TestObservableDict(unittest.TestCase):
    def test_construct(self):
        o = ObservableDict()

    def test_construct_args(self):
        o = ObservableDict({'key': 'value'})
        self.assertEqual({'key': 'value'}, o)

    def test_construct_args_observers(self):
        observers = []
        o = ObservableDict({'key': 'value'}, key2='value2', observers=observers)
        self.assertEqual({'key': 'value', 'key2': 'value2'}, o)

    def test_notify(self):
        updates = []
        o = ObservableDict()
        o.add_observers(updates.append)
        self.assertEqual([], updates)
        o['key'] = 'value'
        self.assertEqual([o.Update(o, 'key', None, 'value')], updates)

    def test_notify_initial_observers(self):
        updates = []
        o = ObservableDict({'key': 'value'}, observers=[updates.append])
        self.assertEqual([], updates)

    def test_notify_initial_observers_pre_notify(self):
        updates = []
        o = ObservableDict({'key': 'value'}, observers=[updates.append], pre_notify=True)
        self.assertEqual([o.Update(o, 'key', None, 'value')], updates)


if __name__ == '__main__':
    unittest.main()
