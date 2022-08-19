import dataclasses


class ObservableDict(dict):
    def __init__(self, *args, **kwargs):
        """Dictionary which updates observers about changes.

        Overrides __setitem__() to send updates to registered observers.
        Observers take the form of a function accepting one :class:`Update`
        instance.

        Observers are only notified when an item is added or replaced, not
        when an item is accessed or when the stored value changes.

        Nested ObservableDict instances do not inherit observers.

        :param observers: List of callables to receive Update instances when a
            field changes.
        :type observers: list, optional
        :param pre_notify: Notify given observers about the initial state of
            the dictionary, defaults to False
            Useful to interpret initial object state the same way as update
            notifications.
        :type pre_notify: bool, optional
        """
        observers = kwargs.pop('observers', [])
        pre_notify_observers = kwargs.pop('pre_notify', False)

        super().__init__(*args, **kwargs)

        self.observers = observers

        if pre_notify_observers:
            for key, value in self.items():
                update = self.Update(self, key, None, value)
                self.update_observers(update)

    def __setitem__(self, key, value):
        old_value = super().get(key)
        super().__setitem__(key, value)
        update = self.Update(self, key, old_value, value)
        self.update_observers(update)

    def update_observers(self, update):
        for observer in self.observers:
            try:
                # Call observer passing the update
                observer(update)
            except Exception as e:
                print(e)

    @dataclasses.dataclass
    class Update:
        """Update about a dictionary field update.

        :ivar source_dict: The observed dictionary
        :ivar key: The key being modified
        :ivar old_value: The value being replaced
        :ivar new_value: The replacement value
        """
        source_dict: 'ObservableDict'
        key: ...
        old_value: ...
        new_value: ...
