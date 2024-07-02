import pandas as pd


class BookLover:

    def __init__(self, name: str, email: str, fav_genre: str):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({
            'book_name': [],
            'book_rating': []
        })

    def add_book(self, book_name: str, rating: int):
        if book_name not in self.book_list['book_name'].to_list():
            # self.book_list = pd.concat()
            self.book_list.loc[len(self.book_list)] = [book_name, rating]
            self.num_books += 1
            print("Book successfully added.")
        else:
            print(f"The book called {book_name} already exists in the book list!")

    def has_read(self, book_name: str) -> bool:
        if book_name in self.book_list['book_name'].to_list():
            return True
        else:
            return False

    def num_books_read(self) -> int:
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3].copy()



if __name__ == "__main__":
    o = BookLover('Doruk', 'abcd@gmail.com', 'Action')
    o.add_book("kitap", 1)
    o.add_book("Ayca", 4)
    o.add_book("Kayhan", 5)
    o.add_book("Dila", 4)
    o.add_book("Tombik", 2)
    print(o.num_books_read())
    print(o.has_read("kitap"))
    print(o.book_list)
    print(o.fav_books())





