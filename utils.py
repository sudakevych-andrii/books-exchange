def filter_books_by_args(args_obj, data):
    if any(args_obj.values()):
        for key, value in args_obj.items():
            if value:
                return data.query.filter(getattr(data, key) == value).all()
    else:
        return data.query.all()
