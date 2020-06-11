class TablePrinter(object):
    def __init__(self, formatter):
        self.formatter = formatter

    def print_table(self, objects, col_names):
        """
        Make a nicely formatted table showing attributes from a list of objects
        """

        self.formatter.headings(col_names)
        for obj in objects:
            row_data = [obj[col_name] for col_name in col_names]
            self.formatter.row(row_data)
