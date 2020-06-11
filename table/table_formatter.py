from abc import ABC, abstractmethod


class TableFormatter(ABC):

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, row_data):
        pass
