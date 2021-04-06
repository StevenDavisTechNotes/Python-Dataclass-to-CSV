from typing import List, Type, TypeVar, TextIO

from .CSVDataclassTableWriter import CSVDataclassTableWriter

U = TypeVar('U')


def WriteDataclassList(outputLogFile: TextIO, rows: List[U], t: Type[U]):
    CSVDataclassTableWriter[t](
        rows).write_file(outputLogFile)
