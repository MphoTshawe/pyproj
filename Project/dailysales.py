
from datetime import datetime

class DailySales:
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, date, region, amount):
        self.date = datetime.strptime(date, self.DATE_FORMAT)
        self.region = region
        self.amount = amount
        self.quarter = self.calculate_quarter()

    def calculate_total_sales(sales_list):
        total = 0
        for sale in sales_list:
             total += sale['Amount']
        return total



    def calculate_quarter(self):
        month = self.date.month
        if 1 <= month <= 3:
            return "Q1"
        elif 4 <= month <= 6:
            return "Q2"
        elif 7 <= month <= 9:
            return "Q3"
        else:
            return "Q4"

    def to_list(self):
        return [self.date.strftime(self.DATE_FORMAT), self.quarter, self.region, str(self.amount),]

    def is_valid(self):
        
        if self.date > datetime.now():
            return False
        
        if self.region not in ['w', 'm', 'c', 'e']:
            return False
        
        if self.amount <= 0:
            return False
        return True
