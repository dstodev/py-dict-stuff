import unittest

from observable_dict import ObservableDict, DictUpdate


class TestObservableMapping(unittest.TestCase):
    def test_notify(self):
        updates = []
        def callback(update: DictUpdate): updates.append(update)
        o = ObservableDict()
        o.observers.append(callback)
        self.assertEqual([], updates)
        o['key'] = 'value'
        self.assertEqual([DictUpdate(o, 'key', None, 'value')], updates)

        # TODO: Test:
        #   construct with args
        #   construct with args and constructor broadcasts all initial updates to provided observers
        #       This behavior is useful so that the initial object state does not need to be interpreted
        #       separately from update notifications--instead, only update notifications need to be
        #       interpreted, and that interpreter can be primed with initial DictUpdate instances.


if __name__ == '__main__':
    unittest.main()
