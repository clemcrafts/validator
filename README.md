# File Validation Pipeline



## Run the application locally

Create a virtual environment:

`virtualenv env -p python3.8`

Source it:

`source env/bin/activate`

Install the libraries:

`pip install -r requirements.txt`

Launch the validator:

`python validator.py`

## Launch the unit tests

To launch the unit tests:

```python -m pytest tests```

## Launch integration tests

```
behave tests/integration_tests/features
```

It will run the validator against various test CSVs:

```
Scenario: A valid CSV is validated by the Machine Learning pipeline
  When the pipeline ingests a valid CSV
  Then the pipeline validates it with no error

Scenario: An invalid CSV is invalidated by the Machine Learning pipeline
  When the pipeline ingests an invalid CSV
  Then the pipeline validates it and raises errors

Scenario: An invalid CSV with NANs is invalidated by the Machine Learning pipeline
  When the pipeline ingests an invalid CSV with NANs
  Then the pipeline validates it and raises errors

Scenario: An invalid CSV with invalid accounts is invalidated by the Machine Learning pipeline
  When the pipeline ingests an invalid CSV with invalid accounts
  Then the pipeline validates it and raises errors

Scenario: An invalid CSV with duplicates is invalidated by the Machine Learning pipeline
  When the pipeline ingests an invalid CSV with duplicates
  Then the pipeline validates it and raises errors
```

## Launch the load tests



## Generate the Swagger contract

To generate the documentation of the data contract based on the code, run:

```
python spec.py
```

It gives the following Swagger file:

![alt tag](https://i.ibb.co/6njYkm2/Screenshot-2022-01-29-at-02-15-40.png)


This file can be uploaded automatically in Confluence with the right plugin so the stakeholders and the developers share the same (reduces the risk of misunderstanding).
