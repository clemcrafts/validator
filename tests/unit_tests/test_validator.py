from validator.validator import Validator
from unittest.mock import Mock, call
from pyspark.sql import SparkSession
from .mocked_data import *
from copy import copy
import pandas as pd
import pytest


@pytest.fixture
def spark():
    return SparkSession.builder.getOrCreate()


@pytest.fixture
def validator(monkeypatch):
    """
    We mock the spark context and session to test only the validation steps.
    :param obj monkeypatch: a monkeypatch instance for the mocking.
    :return obj validator: a validator instance for the validation.
    """
    monkeypatch.setattr("validator.validator.SparkSession", Mock())
    monkeypatch.setattr("validator.validator.SparkContext", Mock())
    return Validator()


def test_valid_header(spark, validator):
    """
    Testing that a valid header does not raise errors.
    """
    validator.dataframe = spark.createDataFrame([VALID_DATAFRAME])
    print(validator.dataframe)
    validator._validate_header()


@pytest.mark.parametrize(
    'header',
    [INVALID_HEADER_FIELD_MISSING,
     INVALID_HEADER_EXTRA_SPACE,
     INVALID_HEADER_WRONG_DELIMITER,
     INVALID_HEADER_EXTRA_FIELD])
def test_invalid_headers(spark, validator, header):
    """
    Testing that an invalid header is raising an error.
    """
    validator.dataframe = spark.createDataFrame([header])
    print(validator.dataframe)
    with pytest.raises(ValueError):
        validator._validate_header()


def test_valid_data(spark, validator):
    """
    Testing that a valid header does not raise errors.
    """
    validator.dataframe = spark.createDataFrame([VALID_DATAFRAME])
    print(validator.dataframe)
    validator._validate_data_contract()


@pytest.mark.parametrize(
    'data',
    [INVALID_DATA_WITH_NAN,
     INVALID_DATA_WITH_INVALID_DATES,
     INVALID_DATA_WITH_INVALID_ACCOUNTS])
def test_invalid_data(spark, validator, data):
    """
    Testing that invalid data is raising an error.
    """
    validator.dataframe = spark.createDataFrame([data])
    print(validator.dataframe)
    with pytest.raises(ValueError):
        validator._validate_data_contract()


def test_data_with_full_duplicates(spark, validator):
    """
    Testing that invalid data with duplicates is raising an error.
    """
    validator.dataframe = spark.createDataFrame(
        [VALID_DATAFRAME, VALID_DATAFRAME])
    print(validator.dataframe)
    with pytest.raises(ValueError):
        validator._validate_duplicates()


def test_data_with_partial_duplicates(spark, validator):
    """
    Testing that invalid data with partial duplicates is raising an error.
    """
    partial_duplicate = copy(VALID_DATAFRAME)
    partial_duplicate["age"] = str(int(VALID_DATAFRAME["age"]) + 2)
    validator.dataframe = spark.createDataFrame(
        [VALID_DATAFRAME, partial_duplicate])
    print(validator.dataframe)
    with pytest.raises(ValueError):
        validator._validate_duplicates()
