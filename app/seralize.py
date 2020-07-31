from extensions.extensions import ma
from app.model import User
from marshmallow import validate, fields


class ProductSchema(ma.SQLAlchemyAutoSchema):
    name = fields.String(required=True, validate=[
                         validate.Length(min=2, max=20)])
    category_id = fields.Integer(required=True)

    class Meta:
        model = Product
        load_instance = True


class CategorySchema(ma.SQLAlchemyAutoSchema):
    name = fields.String(required=True, validate=[
                         validate.Length(min=2, max=20)])

    class Meta:
        model = Category
        load_instance = True
