import collections.abc as abc
from typing import Iterator


class ObservableMapping(abc.MutableMapping):
    def __setitem__(self, key, value):
        pass

    def __delitem__(self, index):
        pass

    def __getitem__(self, key):
        pass

    def __len__(self) -> int:
        pass

    def __iter__(self) -> Iterator:
        pass
