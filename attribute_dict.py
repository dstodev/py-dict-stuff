class AttributeDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, *args):
        assert len(args) == 1
        key = args[0]
        value = super().setdefault(key, AttributeDict())
        if self.is_convertible(value):
            value = AttributeDict(value)
            super().__setitem__(key, value)
        return value

    @staticmethod
    def is_convertible(obj):
        return type(obj) is dict

    def __setattr__(self, key, value):
        if self.is_convertible(value):
            value = AttributeDict(value)
        super().__setitem__(key, value)

    __delattr__ = dict.__delitem__
