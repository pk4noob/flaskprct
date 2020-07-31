from app_init.app_factory import createAp
from flask import jsonify, current_app, request
from http import HTTPStatus
import os
import warnings
from flask import Flask, request, jsonify
from app.seralize import ProductSchema, CategorySchema
from app.model import Product, Category
from http import HTTPStatus
from marshmallow import ValidationError

warnings.simplefilter("ignore")
settings_name = os.getenv("settings")
app = createAp(settings_name)


@app.route("/product", methods=["POST"])
def createPost():
    data = request.get_json()
    try:
        x = ProductSchema().load(data)
        x.pasword_hash()
        x.savedb()
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    return ProductSchema().jsonify(x), HTTPStatus.OK


@app.route("/product/<int:id>", methods=["GET"])
def createget(id):
    dataa = Product.query.filter_by(id=id).first()
    if dataa:
        return ProductSchema().jsonify(dataa), HTTPStatus.OK
    return jsonify(msg="Error"), HTTPStatus.NOT_FOUND


@app.route("/product", methods=["GET"])
def createAll():
    dataAll = Product.query.all()
    return ProductSchema().jsonify(dataAll, many=True), HTTPStatus.OK


@app.route("/product/<int:id>", methods=["PUT"])
def updateMethods(id):
    dataupdate = Product.query.filter_by(id=id).first()
    if dataupdate:
        dataa = request.get_json()
        dataupdate.update(**dataa)
        return ProductSchema().jsonify(dataa), HTTPStatus.OK
    return jsonify(msg="error"), HTTPStatus.BAD_REQUEST


@app.route("/product/<int:id>", methods=["DELETE"])
def deleteMethods(id):
    delet = Product.query.filter_by(id=id).first()
    if delet:
        delet.deletedb()
        return jsonify(messege="silindi"), HTTPStatus.OK
    return jsonify(messege="silindiii"), HTTPStatus.bad


@app.route("/category", methods=["POST"])
def createPost():
    data = request.get_json()
    try:
        x = CategorySchema().load(data)
        x.pasword_hash()
        x.savedb()
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    return CategorySchema().jsonify(x), HTTPStatus.OK


@app.route("/category/<int:id>", methods=["GET"])
def createget(id):
    dataa = Category.query.filter_by(id=id).first()
    if dataa:
        return CategorySchema().jsonify(dataa), HTTPStatus.OK
    return jsonify(msg="Error"), HTTPStatus.NOT_FOUND


@app.route("/category", methods=["GET"])
def createAll():
    dataAll = Category.query.all()
    return CategorySchema().jsonify(dataAll, many=True), HTTPStatus.OK


@app.route("/category/<int:id>", methods=["PUT"])
def updateMethods(id):
    dataupdate = Category.query.filter_by(id=id).first()
    if dataupdate:
        dataa = request.get_json()
        dataupdate.update(**dataa)
        return CategorySchema().jsonify(dataa), HTTPStatus.OK
    return jsonify(msg="error"), HTTPStatus.BAD_REQUEST


@app.route("/category/<int:id>", methods=["DELETE"])
def deleteMethods(id):
    delet = Category.query.filter_by(id=id).first()
    if delet:
        delet.deletedb()
        return jsonify(messege="silindi"), HTTPStatus.OK
    return jsonify(messege="silindiii"), HTTPStatus.bad
