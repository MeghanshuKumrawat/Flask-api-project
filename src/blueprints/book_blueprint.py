from flask import Blueprint, jsonify, request
from ..db.models import Book, Transaction
from mongoengine.queryset.visitor import Q

# define the blueprint
book_blueprint = Blueprint(name="book_blueprint", import_name=__name__)


# list of all the books with that name or term in the book name
@book_blueprint.route('/book-search', methods=['GET'])
def search_book():
    try:
        data = Book.objects(name__icontains=request.args.get('book', ''))
    except Exception as e:
        data = {"message":"request failed!",
                "request":"GET",
                "parameters help":"book name or a term in the name of the book",
                "parameters required":"?book=example",
                "exception":e}
    return jsonify(data)

# list of books with rent in that range
@book_blueprint.route('/book-price-range', methods=['GET'])
def range_book():
    try:
        price_range = request.args.get('price_range').split('-')
        data = Book.objects((Q(rent__gte=int(price_range[0])) & Q(rent__lte=int(price_range[1]))))
    except Exception as e:
        data = {"message":"request failed!",
                "request":"GET",
                "parameters help":"rent price range",
                "parameters required":"?price_range=10-20",
                "exception":e}
    return jsonify(data)


# list of books with matching values as in input
@book_blueprint.route('/filter-book', methods=['GET'])
def filter_book():
    try:
        title = request.args.get('title')
        category = request.args.get('category')
        price_range = request.args.get('price_range').split('-')
        data = Book.objects((Q(name__icontains=title) & Q(category__icontains=category) & Q(rent__gte=int(price_range[0])) & Q(rent__lte=int(price_range[1]))))
    except Exception as e:
        data = {"message":"request failed!",
                "request":"GET",
                "parameters help":"category + name/term + rent per day(range)",
                "parameters required":"?category=data_science&title=data smart&price_range=10-100",
                "exception":e}
    return jsonify(data)

