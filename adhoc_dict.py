from typing import Any


class AdhocDict(dict):
    def __getitem__(self, item: Any):
        value = self.get(item, None)
        if value is None:
            value = self.__class__()
            self.__setitem__(item, value)
        return value
