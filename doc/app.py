from flask import Flask

app = Flask(__name__)

@app.route('/example', methods=['GET'])
def get_example():
    return {'message': 'Successful response'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
