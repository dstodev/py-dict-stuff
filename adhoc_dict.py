class AdhocDict(dict):
    def __getitem__(self, *args):
        assert len(args) == 1
        key = args[0]
        value = super().get(key)
        if value is None:
            value = self.__class__()
            super().__setitem__(key, value)
        return value
