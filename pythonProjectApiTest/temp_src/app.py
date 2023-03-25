from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟一个数据库
books = [
    {
        'id': 1,
        'title': 'Python编程：从入门到实践',
        'author': 'Eric Matthes',
        'publication_date': '2016-11-01',
    },
    {
        'id': 2,
        'title': '流畅的Python',
        'author': 'Luciano Ramalho',
        'publication_date': '2018-07-20',
    }
]


# 获取所有书籍
@app.route('/api/books', methods=['GET'])
def get_books():
    response = jsonify({'books': books})

    # 从请求头中获取 Cookie
    # 第一次请求设置user_id 可以理解token
    user_id = request.cookies.get('user_id')
    if not user_id:
        response.set_cookie('user_id', '123456')

    response.set_cookie('user_id', user_id)

    response.headers['Content-Type'] = 'application/json; charset=utf-8'

    return response


# 新增书籍
@app.route('/api/books', methods=['POST'])
def add_book():
    if not request.json or not 'title' in request.json:
        return jsonify({'message': 'Title is required.'}), 400

    book = {
        'id': max(b['id'] for b in books) + 1,
        'title': request.json['title'],
        'author': request.json.get('author', ''),
        'publication_date': request.json.get('publication_date', ''),
    }
    books.append(book)

    response = jsonify({'book': book})

    user_id = request.cookies.get('user_id')
    if not user_id:
        response.set_cookie('user_id', '123456')

    response.set_cookie('user_id', user_id)

    return response, 201


if __name__ == '__main__':
    app.run(debug=True)
