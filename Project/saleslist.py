
from dailysales import DailySales

class SalesList:
    def __init__(self):
        self.sales_list = []
        

    def add_sales_record(self, sales_record):
        if sales_record.is_valid():
            self.sales_list.append(sales_record)

    def get_sales_record_by_index(self, index):
        if 0 <= index < len(self.sales_list):
            return self.sales_list[index]

    def add_from_another_sales_list(self, another_sales_list):
        for sales_record in another_sales_list.sales_list:
            self.add_sales_record(sales_record)

    def __len__(self):
        return len(self.sales_list)

    def __iter__(self):
        return iter(self.sales_list)
