import pandas as pd
from datetime import datetime

# Example Data
books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925, 'genre': 'Fiction'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'genre': 'Fiction'},
    {'title': '1984 Romance', 'author': 'George Orwell', 'year': 1949, 'genre': 'Science Fiction'},
    {'title': 'The Hunger Games', 'author': 'Suzanne Collins', 'year': 2008, 'genre': 'Science Fiction'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year': 1813, 'genre': 'Romance'}
]

# Make DataFrame
df = pd.DataFrame(books)

# Task 1: recent book last 10 year
def recent_books(book_df):
    current_year = datetime.now().year
    return book_df[book_df['year'] >= current_year - 10]

# task 2: search function
def search_books(keyword):
    filtered_books = df[df['title'].str.contains(keyword, case=False) | df['genre'].str.contains(keyword, case=False)]
    return filtered_books.to_dict(orient='records')

# example usage
recent_books_df = recent_books(df)
search_result = search_books("gatsby")


print("Buku Terbaru:", recent_books_df)
print("Hasil Pencarian:", search_result)
