
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  
from regions import Regions
from files import File
from files import FileImportError
from dailysales import DailySales
from saleslist import SalesList
from decimal import Decimal 

regions = Regions()
regions.add_region('w', 'West')
regions.add_region('m', 'Mountain')
regions.add_region('c', 'Central')
regions.add_region('e', 'East')


sales_data = SalesList()
file_path = []

while True:
    print("\nCOMMAND MENU")
    print("1. View all sales")
    print("2. Add a sale")
    print("3. Import sales from file")
    print("4. Menu")
    print("5. Exit program")

    choice = input("Please enter a command: ")

    if choice == "view":
        print("\nAll Sales:")
        print(" Date      Quater    Region   Amount ")
        print("===============================================================")
        for i, sales_record in enumerate(sales_data, 1):
            print(f"{i}.  {sales_record.date.strftime('%Y-%m-%d')},  {sales_record.quarter}, "
                  f" {regions.get_region_by_code(sales_record.region).name}, "
                    f" {sales_record.amount}") 
           
        print("==================================================================")
       
        total_amount = sum(sale_record.amount for sale_record in sales_data) 
        print(f'Total Sales Amount: {locale.currency (total_amount)}')
            
    elif choice == "add":
        date_input = input("Date (YYYY-MM-DD): ")
        region_input = input(f"Region ({regions}): ")
        amount_input = input("Amount: ")
        
        if region_input in regions.get_valid_region_codes():
            sales_record = DailySales(date_input, region_input, Decimal(amount_input))
            if sales_record.is_valid():
                sales_data.add_sales_record(sales_record)
                print(f"Sale for {sales_record.date.strftime('%Y-%m-%d')} added to {sales_record.quarter}.")
            else:
                print("Invalid sale data. Please check the format.")
        else:
            print("Invalid region code. Please choose a valid region.")
    elif choice == "import":
        file_name = input("Enter name of file to import: ")
        try:
            file = File(file_name, None)  
            if file.is_valid_filename() and not file.is_file_already_imported() and file.is_file_found():
                try:
                     with open(file_name, "r") as file:
       
                       file_contents = file.read()
                       print(file_contents)
                except FileImportError as e:
                    print(f"File Import Error: {e}")           
                print("Data imported successfully.")
            else:
                print("Invalid file or file already imported.")
        except FileImportError as e:
            print(f"File Import Error: {e}")
    elif choice == "menu":
        continue
    elif choice == "exit":
        print("Exiting program.")
        break
    else:
        print("Invalid command. Please try again.")
