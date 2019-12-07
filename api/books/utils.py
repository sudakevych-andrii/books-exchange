def filter_books_by_args(args_obj, data):
    if any(args_obj.values()):
        for key, value in args_obj.items():
            if value:
                return data.query.filter(getattr(data, key) == value).all()
    else:
        return data.query.filter(data.visibility == 1).order_by(data.id).all()


def add_book_to_library(user, book):
    user.library.append(book)


def add_book_to_wishlist(user, book):
    user.wishlist.append(book)
