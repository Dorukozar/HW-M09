import unittest
from booklover.booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        test_object = BookLover("Doruk", "abcd@gmail.com", "Action")
        test_object.add_book("Microeconomics", 5)
        self.assertIn("Microeconomics", test_object.book_list['book_name'].to_list())

    def test_2_add_book(self):
        test_object = BookLover("Doruk", "abcd@gmail.com", "Action")
        test_object.add_book("Microeconomics", 5)
        test_object.add_book("Microeconomics", 5)
        self.assertEqual(1, test_object.book_list['book_name'].to_list().count("Microeconomics"))


    def test_3_has_read(self):
        test_object = BookLover("Doruk", "abcd@gmail.com", "Action")
        test_object.add_book("Microeconomics", 5)
        self.assertTrue(test_object.has_read('Microeconomics'))

    def test_4_has_read(self):
        test_object = BookLover("Doruk", "abcd@gmail.com", "Action")
        test_object.add_book("Microeconomics", 5)
        self.assertFalse(test_object.has_read('Not Here'))


    def test_5_num_books_read(self):
        test_object = BookLover("Doruk", "abcd@gmail.com", "Action")
        test_object.add_book("Book 1", 1)
        test_object.add_book("Book 2", 4)
        test_object.add_book("Book 3", 5)
        test_object.add_book("Book 4", 4)
        test_object.add_book("Book 5", 2)
        self.assertEqual(5, test_object.num_books_read())


    def test_6_fav_books(self):
        test_object = BookLover("Doruk", "abcd@gmail.com", "Action")
        test_object.add_book("Book 1", 1)
        test_object.add_book("Book 2", 4)
        test_object.add_book("Book 3", 5)
        test_object.add_book("Book 4", 4)
        test_object.add_book("Book 5", 2)
        test_object.add_book("Book 6", 2)
        test_object.add_book("Book 7", 1)
        test_object.add_book("Book 8", 5)
        test_object.add_book("Book 9", 4)
        [self.assertGreater(rating, 3) for rating in test_object.fav_books()['book_rating'].to_list()]


if __name__ == '__main__':
    unittest.main(verbosity=3)







