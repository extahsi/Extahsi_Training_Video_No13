# src/app.py

from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Welcome(Resource):
    def get(self):
        return jsonify({
            "message": "Welcome to Extahsi Vulnerability and Exploit Training"
        })

api.add_resource(Welcome, '/')

if __name__ == '__main__':
    app.run(debug=True)
