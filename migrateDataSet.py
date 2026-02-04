import pandas as pd
from sqlalchemy import create_engine

from database import DATABASE_URL

def migrate_to_postgre():
    #load the csv file
    print("Reading the books.csv")
    df = pd.read_csv("books.csv", sep=';', encoding='latin-1', on_bad_lines='skip')

    df = df.rename(columns={
        'ISBN': 'isbn',
        'Book-Title': 'title',
        'Book-Author': 'author',
        'Year-Of-Publication': 'year',
        'Publisher': 'publisher',
        'Image-URL-M': 'image_url'
        })
    #keep only the columns that match your db
    df = df[['isbn', 'title', 'author', 'year', 'publisher', 'image_url']]

    #cleaning the year column
    df['year'] = pd.to_numeric(df['year'],errors='coerce').fillna(0).astype(int)

    engine = create_engine(DATABASE_URL)

    print(f'Uploading {len(df)} books to postgre')

    try:
        df.to_sql('books', con=engine, if_exists='append', index=False,chunksize=1000)
        print('Success!! Your full dataset is now uploaded')
    except UnicodeDecodeError:
        print("Encoding error: Try using encoding='cp1252' if latin-1 fails.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    migrate_to_postgre()







