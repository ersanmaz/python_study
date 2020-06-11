from table.table_formatter import TableFormatter


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, row_data):
        print(','.join(row_data))
