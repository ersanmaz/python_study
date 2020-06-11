from table.table_formatter import TableFormatter


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>{}</th>'.format(h), end='')
        print('</tr>')

    def row(self, row_data):
        print('<tr>', end='')
        for d in row_data:
            print('<td>{}</td>'.format(d), end='')
        print('</tr>')
