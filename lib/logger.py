from typing import List

from prettytable import PrettyTable

from lib.file import FileHandler


class Logger:

    @staticmethod
    def print_table(headers: List[str], rows: List[List[str]]) -> None:
        print(Logger.__create_table(headers, rows))

    @staticmethod
    def write_table_to_file(file: FileHandler, headers: List[str], rows: List[List[str]]) -> None:
        table = Logger.__create_table(headers, rows)
        file.write_lines(table.get_string())

    @staticmethod
    def __create_table(headers: List[str], rows: List[List[str]]):
        table = PrettyTable(headers)

        for row in rows:
            table.add_row(row)

        return table
