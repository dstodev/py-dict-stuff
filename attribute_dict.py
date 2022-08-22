from typing import Any

from adhoc_dict import AdhocDict
from convert_dict import ConvertDict


class AttributeDict(AdhocDict, ConvertDict):
    def __getattr__(self, name: str) -> Any:
        return super().get(name)

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setitem__(name, value)

    def __delattr__(self, name: str) -> None:
        super().__delitem__(name)
