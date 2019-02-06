import numpy as np
import pandas as pd

class Book():
    def __init__(self, id=0,
                 goodreads_id=0,
                 authors='',
                 title='',
                 original_title='',
                 publication_year=0,
                 average_rating=0,
                 ratings_count=0,
                 ratings_1=0,
                 ratings_2=0,
                 ratings_3=0,
                 ratings_4=0,
                 ratings_5=0,
                 image_url='',
                 small_image_url=''):
        self.id = id
        self.goodreads_id = goodreads_id
        self.authors_str = authors
        self.authors = authors.split(', ')
        self.title = str(title)
        self.original_title = str(original_title)
        # If the original title is missing, use the title instead
        if self.original_title == 'nan':
            self.original_title = self.title
        self.publication_year = publication_year
        self.average_rating = average_rating
        self.ratings_count = ratings_count
        self.ratings_1 = ratings_1
        self.ratings_2 = ratings_2
        self.ratings_3 = ratings_3
        self.ratings_4 = ratings_4
        self.ratings_5 = ratings_5
        self.image_url = image_url
        self.small_image_url = small_image_url

    def __repr__(self):
        return self.title + ' by ' + self.authors_str
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.id == other.id
        return False

class BookDatabase():
    id_dict = {}

    @classmethod
    def initialize_dicts(cls):
        books = pd.read_csv('./data/books.csv')
        books.apply(cls._add_book_from_pd, axis=1)

    @classmethod
    def _add_book_from_pd(cls, book):
        cls.id_dict[book.book_id] = Book(id=book.book_id,
                                         goodreads_id=book.goodreads_book_id,
                                         authors=book.authors,
                                         title=book.title,
                                         original_title=book.original_title,
                                         publication_year=book.original_publication_year,
                                         average_rating=book.average_rating,
                                         ratings_count=book.ratings_count,
                                         ratings_1=book.ratings_1,
                                         ratings_2=book.ratings_2,
                                         ratings_3=book.ratings_3,
                                         ratings_4=book.ratings_4,
                                         ratings_5=book.ratings_5,
                                         image_url=book.image_url,
                                         small_image_url=book.small_image_url)

    @classmethod
    def search(cls, search_string):
        results = []
        search_string = search_string.lower()
        for book in cls.id_dict.values():
            if search_string in book.title.lower() or search_string in book.original_title.lower():
                results.append(book)
        if len(results) == 0:
            return 'Not found'
        return results

    @classmethod
    def get_book_by_id(cls, id):
        if id not in cls.id_dict:
            return 'Not found'
        return cls.id_dict[id]