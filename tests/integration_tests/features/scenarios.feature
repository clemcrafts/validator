@fixture.pipeline.up
Feature: The Machine Learning Pipeline Validates Data

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
