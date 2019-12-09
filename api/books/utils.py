from db import db


def filter_books_by_args(args_obj, data):
    if any(args_obj.values()):
        for key, value in args_obj.items():
            if value:
                return data.query.filter(getattr(data, key) == value).all()
    else:
        return data.query.all()


def show_books(args_obj, data, user):
    data = filter_books_by_args(args_obj, data)
    if user and user.role == "admin":
        return data
    else:
        return [book for book in data if book.visibility]


def add_book_to_library(user, book):
    user.library.append(book)
    if book in user.wishlist:
        user.wishlist.remove(book)
    db.session.commit()
    return user.library


def add_book_to_wishlist(user, book):
    user.wishlist.append(book)
    db.session.commit()
    return user.wishlist
