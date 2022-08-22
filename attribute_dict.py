from typing import Any


class AttributeDict(dict):
    def __init__(self, *args, **kwargs) -> None:
        convert_dict = kwargs.pop('convert_dict', False)

        super().__init__(*args, **kwargs)

        if convert_dict:
            for key, value in self.items():
                super().__setitem__(key, self.convert_dict(value))

    @classmethod
    def convert_dict(cls, value: Any) -> Any:
        if type(value) is dict:
            for key, inner_value in value.items():
                value[key] = cls.convert_dict(inner_value)
            return cls(value)
        else:
            return value

    def __getattr__(self, name: str) -> Any:
        return super().get(name)

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setitem__(name, value)

    def __delattr__(self, name: str) -> None:
        super().__delitem__(name)
