
import os
from flask import Flask
from flask import jsonify
from buzz import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

@app.route("/users")
def get_user():
    
    return jsonify(
        username="Nick",
        email="Nick.CHlam@rht.com",
        id=45
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))