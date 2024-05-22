import os, sys, django, requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_app.settings")
from django.conf import settings
sys.path.append( settings.BASE_DIR )
django.setup()

from django.test import TestCase
from web.models import User,Post,Publisher,Author,Book


# def list_all_users():
    
#     all_users = User.objects.all()
#     for user in all_users:
#         print(f"Name: {user.name}, Email: {user.email}, Place: {user.place}")

# list_all_users()


def post_list_select_related():
    posts = Post.objects.select_related('user').all()

    for post in posts:
        print(f"Title: {post.title}, User: {post.user.name}, User Email: {post.user.email}")

post_list_select_related() 

def users_list_with_post_prefetch_related():
    users = User.objects.prefetch_related('posts').all()
    for user in users:
        posts = user.posts.all()
        print(user.name,[post.title for post in posts])

users_list_with_post_prefetch_related()


def book_list_select_related():
    #books along with their author and publsher
    books = Book.objects.select_related('author__publisher').all()
    for book in books:
        print(book.title, book.author.name, book.author.publisher.name)

book_list_select_related()

def authors_with_theirbookgenre_prefetch_related():
    #retrive authors with their books and genre of those books
    authors = Author.objects.prefetch_related('books__genre').all()

    for author in authors:
        for book in author.books.all():
            genre = [genre.name for genre in book.genre.all()]
            print(f"Author: {author.name}, Book: {book.title}, Genre: {genre}")

authors_with_theirbookgenre_prefetch_related()