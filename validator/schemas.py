from marshmallow_pyspark import Schema
from marshmallow import fields, validates_schema
from marshmallow.validate import OneOf, NoneOf
from .config import VALID_ACCOUNTS


class Entry(Schema):
    """
    A validation schema for one row of the CSV data.
    """
    guid = fields.Str(required=True)
    age = fields.Int(required=True)
    signup_date = fields.DateTime(required=True, format="%M/%d/%Y")
    birthday = fields.DateTime(required=True, format="%m/%d/%Y")
    account_type = fields.Str(validate=OneOf(VALID_ACCOUNTS), required=True)
