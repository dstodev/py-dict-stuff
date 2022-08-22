from typing import Any


class ConvertDict(dict):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        convert = kwargs.pop('convert', True)
        super_init = dict(*args, **kwargs)
        if convert:
            for key, value in super_init.items():
                super_init[key] = self.convert_dict(value)
        super().__init__(super_init)

    @classmethod
    def convert_dict(cls, value: Any) -> Any:
        if type(value) is dict:
            return cls(value, convert=True)
        else:
            return value
