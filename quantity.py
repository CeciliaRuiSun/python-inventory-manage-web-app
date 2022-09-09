from flask import Flask, request, abort
from flask_restful import Resource, Api

from data import items
from marshmallow import Schema, fields
class QtyQuerySchema(Schema):
    category = fields.Str()
    name = fields.Str(required=True)
    quantity = fields.Int()
    owner = fields.Str()

schema = QtyQuerySchema()
class Quantity(Resource):
    def get(self):
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        args = request.args
        start = args['start']
        end = args['end']

        return {'item': list((filter(lambda x: x['quantity'] >= int(start) and x['quantity'] <= int(end), items)))}
