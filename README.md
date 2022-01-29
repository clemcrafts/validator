# File Validation Pipeline

This pipeline is validating a CSV file that will be used by a ML algorithm.

I've tried to show a multi-angle approach:
schemas definition, auto-generated Swagger documentation, unit and integration tests, CI/CD and library packaging.

It would be usable by another module though pip after publishing it.

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

## Generate the Swagger documentation

To generate the documentation of the data contract based on the code, run:

```
python -m validator.spec
```

It generates the following Swagger file in `docs/doc.yml`:

![alt tag](https://i.ibb.co/47yJMWq/Screenshot-2022-01-29-at-19-33-22.png)


This file can be uploaded automatically in Confluence with the right plugin so the stakeholders and the developers share the same (reduces the risk of misunderstanding).

## CI/CD with github actions (workflow)

The CI has been setup with Github workflows (`.github/workflows/main.yml`). 

It is currently building the package and running the tests at every push, see "action" tab on this repository:


![alt tag](https://i.ibb.co/pdm3zjW/Screenshot-2022-01-29-at-18-52-00.png)


## Perspectives

If I had to push the task further, I would: 

- Go for a Dockerized version orchestrated with Kubernetes with auto-scale on CPU/Memory (preparing this to become a standalone fetching from a BLOB storage).
- Prepare the infrastructure as a code with a Terraform module for the deployment.
- Add a load test with locust using large files to demonstrate why using Spark matters for performance.


