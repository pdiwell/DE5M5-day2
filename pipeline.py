import pandas as pd


def import_books():
    df_books_import = pd.read_csv("data/03_Library Systembook.csv")

    df_books_wip = df_books_import[df_books_import['Id'].notnull()]
    
    df_books_wip['book_id'] = df_books_wip['Id'].astype(float).astype('Int64') # Convert to int
    df_books_wip['checkout_date'] = pd.to_datetime(df_books_wip['Book checkout'], format='"%d/%m/%Y"', errors='coerce') # Convert strings to dates
    df_books_wip['weeks_allowed'] = df_books_wip['Days allowed to borrow'].str.split(' ').str[0] # Convert days allowed to borrow to number
    df_books_wip['returned_date'] = pd.to_datetime(df_books_wip['Book Returned'], format='%d/%m/%Y') # Convert strings to dates
    df_books_wip['customer_id'] = df_books_wip['Customer ID'].astype(float) # Convert to float
    
    df_books_wip = df_books_wip.rename(columns = {'Books' : 'book_name'}) # Rename

    df_books = df_books_wip.drop(columns=['Days allowed to borrow', 'Id', 'Book checkout', 'Book Returned', 'Customer ID'])

    return df_books

def import_customers():
    df_customers_import = pd.read_csv("data/03_Library SystemCustomers.csv")

    df_customers_import['customer_id'] = df_customers_import['Customer ID'].astype(float) # Convert IDs to floats

    df_customers_import['customer_name'] = df_customers_import['Customer Name']

    df_customers = df_customers_import.drop(columns=['Customer ID','Customer Name'])

    return df_customers

if __name__ == "__main__":
    df_books = import_books()
    df_customers = import_customers()