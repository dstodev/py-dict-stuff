import dataclasses


class ObservableDict(dict):
    def __init__(self, *args, **kwargs):
        observers = kwargs.pop('observers', [])
        self.observers = observers
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        old_value = super().get(key)
        super().__setitem__(key, value)
        update = DictUpdate(self, key, old_value, value)
        for observer in self.observers:
            try:
                observer(update)
            except Exception as e:
                print(e)


@dataclasses.dataclass
class DictUpdate:
    source_dict: ObservableDict
    key: ...
    old_value: ...
    new_value: ...
