from typing import Any


class AdhocDict(dict):
    def __getitem__(self, item: Any):
        return self.get(item)

    def get(self, *args: Any) -> Any:
        value = super().get(*args)
        if value is None:
            value = self.__class__()
            self.__setitem__(args[0], value)
        return value
