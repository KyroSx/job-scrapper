from prettytable import PrettyTable


class Logger:

    @staticmethod
    def print_table(headers, rows):
        table = PrettyTable(headers)
        for row in rows:
            table.add_row(row)
        print(table)
