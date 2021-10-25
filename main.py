from logging import debug
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

words = {}

class WebPage(Resource):
    def get(self, url):
        return url

api.add_resource(WebPage, "/webpage/<string:url>")


if __name__=="__main__":
    app.run(debug=True)