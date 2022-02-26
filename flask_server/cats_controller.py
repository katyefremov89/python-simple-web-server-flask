from flask import Flask
from flask import url_for
from flask import json

app = Flask(__name__)


@app.route("/cats", methods=['GET'])
def get_all_cats():
    data = {'func_name': 'get_all_cats'}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/cats/<int:id>")
def get_cat_by_id(id):
    data = {'func_name': 'get_cat_by_id'}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/cats", methods=['POST'])
def create_cat():
    data = {'func_name': 'create_cat'}
    response = app.response_class(
        response=json.dumps(data),
        status=201,
        mimetype='application/json'
    )
    return response


@app.route("/cats/<int:id>", methods=['DELETE'])
def delete_cat_by_id(id):
    data = {'func_name': 'delete_cat_by_id'}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/cats/<int:id>", methods=['PUT'])
def edit_cat(id):
    data = {'func_name': 'edit_cat'}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


with app.test_request_context():
    print(url_for('get_all_cats'))
    print(url_for('get_cat_by_id', id=4))
