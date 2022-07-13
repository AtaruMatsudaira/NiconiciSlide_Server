# -*- coding: utf-8 -*-
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

datas = {}


@app.route('/')
def index():
    return 'hello, world'


@app.route("/AudioUpload", methods=['POST'])
def AudioUpload():
    datas["audios"] = request.form["audios"]
    return make_response(jsonify({'result': True}))


@app.route("/AudioDownload", methods=['GET'])
def AudioDownload():
    return make_response(datas["audios"])


@ app.route("/ImageDownload", methods=['GET'])
def ImageDownload():
    return datas["my_image"]


@ app.route("/ImageUpload/", methods=['GET', 'POST'])
def ImageUpload():
    datas["my_image"] = request.form["images"]
    return make_response(jsonify({'result': True}))


if __name__ == '__main__':
    app.run()
