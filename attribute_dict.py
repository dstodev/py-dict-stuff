class AttributeDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, *args):
        assert len(args) == 1
        key = args[0]
        value = super().setdefault(key, self.__class__())
        if self.is_convertible(value):
            value = self.__class__(value)
            super().__setitem__(key, value)
        return value

    @staticmethod
    def is_convertible(obj):
        # TODO: Expand list of convertible types?
        return type(obj) is dict

    def __setattr__(self, key, value):
        if self.is_convertible(value):
            value = self.__class__(value)
        super().__setitem__(key, value)

    __delattr__ = dict.__delitem__
