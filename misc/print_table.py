import portie
import table

formatter = table.TextTableFormatter()
printer = table.TablePrinter(formatter)
portfolio = portie.read_portfolio('../data/portfolio.csv')
printer.print_table(portfolio, ['name', 'shares'])
