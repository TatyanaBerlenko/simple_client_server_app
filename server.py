from flask import Flask, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello_world():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'


@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.json.get('numbers', [])
    result = sum(map(int, data))
    return f"For numbers {data} The result: {result}"


if __name__ == '__main__':
    app.run(debug=True)