from behave import given, when, then, fixture
from validator.validator import Validator
import pytest


@given('The pipeline is up and running')
def pipeline_running(context):
    """
    Starts the validation pipeline.
    :param obj context: context object being passed through functions.
    """
    context.validator = Validator()

@when('The pipeline ingests a valid CSV')
def pipeline_ingests_valid_csv(context):
    """
    Ingests the valid CSV given in the task.
    :param obj context: context object being passed through functions.
    """
    context.validator.load(
        "tests/integration_tests/features/steps/test_valid_csv.csv")


@when('The pipeline ingests an invalid CSV')
def pipeline_ingests_invalid_csv(context):
    """
    Ingests the invalid CSV given in the task.
    :param obj context: context object being passed through functions.
    """
    context.validator.load(
        "tests/integration_tests/features/steps/test_invalid_csv.csv")


@when('The pipeline ingests an invalid CSV with NANs')
def pipeline_ingests_invalid_csv_with_nans(context):
    """
    Ingests the invalid CSV with NANs values.
    :param obj context: context object being passed through functions.
    """
    context.validator.load(
        "tests/integration_tests/features/steps/test_invalid_csv_nan.csv")

@when('The pipeline ingests an invalid CSV with invalid accounts')
def pipeline_ingests_invalid_csv_with_invalid_accounts(context):
    """
    Ingests the invalid CSV with invalid accounts.
    :param obj context: context object being passed through functions.
    """
    context.validator.load(
        "tests/integration_tests/features/steps/"
        "test_invalid_csv_invalid_accounts.csv")

@when('The pipeline ingests an invalid CSV with duplicates')
def pipeline_ingests_invalid_csv_with_duplicates(context):
    """
    Ingests the invalid CSV with duplicates.
    :param obj context: context object being passed through functions.
    """
    context.validator.load(
        "tests/integration_tests/features/steps/"
        "test_invalid_csv_duplicates.csv")

@then('The pipeline validates it with no error')
def pipeline_validates_without_error(context):
    """
    The validation passed without error.
    :param obj context: context object being passed through functions.
    """
    context.validator.validate()


@then('The pipeline validates it and raises errors')
def pipeline_validates_with_error(context):
    """
    The validation raised errors.
    :param obj context: context object being passed through functions.
    """
    with pytest.raises(ValueError):
        context.validator.validate()