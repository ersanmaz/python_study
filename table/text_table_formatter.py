from table.table_formatter import TableFormatter


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for header in headers:
            print('{:>10s}'.format(header), end=' ')
        print()

    def row(self, row_data):
        for item in row_data:
            print('{:>10s}'.format(str(item)), end=' ')
        print()
