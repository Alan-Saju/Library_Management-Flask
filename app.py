from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data stores
books = [
    {
        'id': 1,
        'title': 'Book One',
        'author': 'Author A',
        'published_year': 2001
    },
    {
        'id': 2,
        'title': 'Book Two',
        'author': 'Author B',
        'published_year': 2002
    }
]

members = [
    {
        'id': 1,
        'name': 'Member One',
        'join_date': '2021-01-01'
    },
    {
        'id': 2,
        'name': 'Member Two',
        'join_date': '2021-02-01'
    }
]

# ID counters
book_id_counter = 3
member_id_counter = 3
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to the Library Management System API. Please use /books or /members endpoints.'})

@app.route('/books', methods=['GET'])
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    start = (page - 1) * per_page
    end = start + per_page

    if title or author:
        results = []
        for book in books:
            if (title and title.lower() in book['title'].lower()) or (author and author.lower() in book['author'].lower()):
                results.append(book)
        return jsonify({'books': results[start:end]})
    else:
        return jsonify({'books': books[start:end]})

@app.route('/books', methods=['POST'])
def add_book():
    global book_id_counter
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    required_fields = ['title', 'author', 'published_year']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    book = {
        'id': book_id_counter,
        'title': data['title'],
        'author': data['author'],
        'published_year': data['published_year']
    }
    books.append(book)
    book_id_counter += 1
    return jsonify(book), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({'message': 'Book deleted'})
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/members', methods=['GET'])
def get_members():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    return jsonify({'members': members[start:end]})

@app.route('/members', methods=['POST'])
def add_member():
    global member_id_counter
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    required_fields = ['name', 'join_date']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    member = {
        'id': member_id_counter,
        'name': data['name'],
        'join_date': data['join_date']
    }
    members.append(member)
    member_id_counter += 1
    return jsonify(member), 201

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = next((m for m in members if m['id'] == member_id), None)
    if member:
        return jsonify(member)
    else:
        return jsonify({'error': 'Member not found'}), 404

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    member = next((m for m in members if m['id'] == member_id), None)
    if member:
        member.update(data)
        return jsonify(member)
    else:
        return jsonify({'error': 'Member not found'}), 404

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = next((m for m in members if m['id'] == member_id), None)
    if member:
        members.remove(member)
        return jsonify({'message': 'Member deleted'})
    else:
        return jsonify({'error': 'Member not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)