from marshmallow_pyspark import Schema
from marshmallow import fields, validates_schema
from marshmallow.validate import OneOf, NoneOf
from .config import VALID_ACCOUNTS


class Entry(Schema):
    """
    A validation schema for one row of the CSV data.
    Various choices have been made here:
    The GUID could be validated as such but the task does not specifies it.
    The dates are validated as date formats suiting pattern from test files.
    All fields are assumed to be required and NaN won't be accepted by the age
    field validator (not an int) nor the dates field validators (not a date).
    As a consequence (and it's better!), no specific checks are performed.
    """
    guid = fields.Str(required=True)
    age = fields.Int(required=True)
    signup_date = fields.DateTime(required=True, format="%M/%d/%Y")
    birthday = fields.DateTime(required=True, format="%m/%d/%Y")
    account_type = fields.Str(validate=OneOf(VALID_ACCOUNTS), required=True)
