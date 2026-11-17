import pandas as pd


def import_books(file_name):
    try:
        df_books_import = pd.read_csv(file_name)
    except Exception as e:
        print(f"Error Occured: {e}")

    record_count_import = len(df_books_import)
    print(f"Book data found and successfully imported {record_count_import} records. Starting data cleanse...")
    
    df_books_import['book_id'] = df_books_import['Id'].astype(float).astype('Int64') # Convert to int
    df_books_import['checkout_date'] = pd.to_datetime(df_books_import['Book checkout'], format='"%d/%m/%Y"', errors='coerce') # Convert strings to dates
    df_books_import['weeks_allowed'] = df_books_import['Days allowed to borrow'].str.split(' ').str[0] # Convert days allowed to borrow to number
    df_books_import['returned_date'] = pd.to_datetime(df_books_import['Book Returned'], format='%d/%m/%Y') # Convert strings to dates
    df_books_import['customer_id'] = df_books_import['Customer ID'].astype(float) # Convert to float

    df_books_nonulls = df_books_import.dropna() # Drop null rows

    nullDrops = len(df_books_import) - len(df_books_nonulls)
    dropCount = nullDrops

    df_books_nodupes = df_books_nonulls.drop_duplicates()
    duplicateBooks = len(df_books_nonulls) - len(df_books_nodupes)
    dropCount += duplicateBooks
    
    df_books_renamed = df_books_nodupes.rename(columns = {'Books' : 'book_name'}) # Rename

    df_books_renamed = df_books_renamed.drop(columns=['Days allowed to borrow', 'Id', 'Book checkout', 'Book Returned', 'Customer ID']) # Drop old column names

    df_books_renamed['loan_duration'] = (df_books_renamed['returned_date'] - df_books_renamed['checkout_date']).dt.days

    df_books_clean = df_books_renamed[df_books_renamed['loan_duration']>=0].reset_index().drop(columns=['index'])
    invalidLoanDrops = len(df_books_nonulls) - len(df_books_clean)
    dropCount += invalidLoanDrops

    print(f"""
Data cleanse completed. Started with {record_count_import} records, {dropCount} rows dropped for the below reasons:
    - {nullDrops} null records
    - {duplicateBooks} duplicate records
    - {invalidLoanDrops} invalid loan durations
Remaining records: {len(df_books_clean)}
    """)

    return df_books_clean

def import_customers(file_name):
    try:
        df_customers_import = pd.read_csv(file_name)
    except Exception as e:
        print(f"Error Occured: {e}")

    record_count_import = len(df_customers_import)
    print(f"Customer data found and successfully imported {record_count_import} records. Starting data cleanse...")
    
    df_customers_nonulls = df_customers_import.dropna()
    nullDrops = len(df_customers_import) - len(df_customers_nonulls)
    dropCount = nullDrops

    df_customers_nodupes = df_customers_nonulls.drop_duplicates()
    duplicateCustomers = len(df_customers_nonulls) - len(df_customers_nodupes)
    dropCount += duplicateCustomers

    df_customers_renamed = df_customers_nodupes.rename(columns = {'Customer Name' : 'customer_name'}) # Rename

    df_customers_renamed['customer_id'] = df_customers_renamed['Customer ID'].astype(float) # Convert IDs to floats

    df_customers = df_customers_renamed.drop(columns=['Customer ID'])

    print(f"""
Data cleanse completed. Started with {len(df_customers_import)} records, {dropCount} rows dropped due to the following reasons:
    - {nullDrops} null records
    - {duplicateCustomers} duplicate records
Remaining records: {len(df_customers)}
""")

    return df_customers

if __name__ == "__main__":
    df_books = import_books("data/03_Library Systembook.csv")
    df_customers = import_customers("data/03_Library SystemCustomers.csv")