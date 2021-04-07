from typing import List, Type, TypeVar, TextIO

from .CSVDataclassTableWriter import CSVDataclassTableWriter

U = TypeVar('U')


def WriteDataclassList(
        outputLogFile: TextIO,
        rows: List[U],
        rowType: Type[U]):
    CSVDataclassTableWriter[rowType](
        rows).write_file(outputLogFile)
