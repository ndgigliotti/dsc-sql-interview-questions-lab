import pandas as pd

def fetch2frame(cursor, index_col=None):
    """Fetch all items from `cursor` and return a DataFrame."""
    columns = [x[0] for x in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    if index_col:
        df.set_index(index_col, inplace=True)
    return df

def fetch_tables(cursor):
    cursor.execute("""SELECT name as table_name
                      FROM sqlite_master 
                      WHERE type ='table'
                      AND name NOT LIKE 'sqlite_%';""")
    return fetch2frame(cursor)
