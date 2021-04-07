import csv
from dataclasses import dataclass, fields
from decimal import Decimal
from enum import Enum
from typing import (
    Any, Generic, List, TextIO, Type, TypeVar, Optional, cast
)

from typing_inspect import get_args, get_generic_type


def decimalToStr(value: Decimal) -> str:
    return str(value)


def enumToStr(value: Enum) -> str:
    return value.name


OBJECT_SERIALIZERS = {
    Decimal: decimalToStr,
    Enum: enumToStr,
}
T = TypeVar('T')


# Adapted from https://mail.python.org/pipermail/python-ideas/2018-October/054281.html  # noqa: E501
@dataclass
class CSVDataclassTableWriter(Generic[T]):
    TableData: List[T]

    @property
    def type_of_T(self) -> Type:
        return get_args(get_generic_type(self))[0]

    @property
    def field_names(self):
        return [
            field.name for field in fields(self.type_of_T)
        ]

    @property
    def record_field(self):
        return fields(self)[0].name

    def to_csv(self, path):
        with open(path, 'w') as file:
            self.write_file(file)

    def write_file(
            self,
            file: TextIO,
            header: Optional[str] = None,
            footer: Optional[str] = None):
        if header is not None:
            file.write(header+'\n')
        writer = csv.writer(cast(Any, file))
        writer.writerow(self.field_names)
        records_field = self.record_field
        writer.writerows(
            self.serialize(record) for record
            in getattr(self, records_field)
        )
        if footer is not None:
            file.write(footer+'\n')

    def serialize(self, record: T):
        for field in fields(record):
            value = getattr(record, field.name)
            serializer = \
                OBJECT_SERIALIZERS.get(field.type, None)
            if serializer:
                value = serializer(value)
            yield value
