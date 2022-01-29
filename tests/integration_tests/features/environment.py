from behave import use_fixture,fixture
from validator.validator import Validator


@fixture(name="fixture.pipeline.up")
def browser_firefox(context, *args, **kwargs):
    context.validator = Validator()
    yield context.validator

def before_tag(context, tag):
    if tag == "fixture.pipeline.up":
        use_fixture(browser_firefox, context, timeout=10)