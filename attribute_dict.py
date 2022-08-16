class AttributeDict(dict):
    def __getattr__(self, *args):
        assert len(args) == 1
        key = args[0]
        value = super().setdefault(key, AttributeDict())
        if self.is_convertible(value):
            value = AttributeDict(value)
            super().__setattr__(key, value)
        return value

    def __setattr__(self, key, value):
        if self.is_convertible(value):
            value = AttributeDict(value)
        super().__setattr__(key, value)

    @staticmethod
    def is_convertible(obj):
        return type(obj) is dict

    __delattr__ = dict.__delitem__
