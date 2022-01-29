from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext
from .schemas import Entry
from .config import DUPLICATION_FIELD_TO_CHECK


class Validator:
    """
    This class is responsible of validating a CSV for a ML pipeline.
    """
    def __init__(self):
        """
        Initialize the validation pipeline.
        """
        self.spark = SparkSession(SparkContext())
        self.dataframe = None

    def load(self, file: str):
        """
        Load the file in a dataframe format. This is does not load the file in
        memory but instantiate a RDD ready to be requested by bits.
        :param str file: the file to use as input of the pipeline.
        """
        self.dataframe = self.spark.read.load(
            file, format="csv", sep=",", header=True)

    def validate(self):
        """
        Validate the CSV file using business rules defined in the task.
        """
        self._validate_header()
        self._validate_data_contract()
        self._validate_duplicates()

    def _validate_header(self):
        """
        Validate the header of the CSV file: it needs to be exactly the same
        as defined in the schema. The order doesn't matter.
        """
        schema, header = list(Entry().fields.keys()), self.dataframe.columns
        schema.sort(), header.sort()
        if schema != header:
            raise ValueError(f"Invalid header {header}. Expected {schema}")

    def _validate_data_contract(self):
        """
        Validate each entry of the CSV file data based on a data schema.
        n.b: the task specifies checks on NaN, we don't need any. These values
        would not be accepted because they're not matching the expected types.
        We verify that in various unit and integration tests.
        """
        df, errors = Entry().validate_df(self.dataframe, unknown='EXCLUDE')
        if len(errors.collect()):
            raise ValueError(errors.collect())

    def _validate_duplicates(self):
        """
        Validate that the file has no duplicates based on specified columns.
        """
        duplicate_count = self.dataframe.groupBy(
                    DUPLICATION_FIELD_TO_CHECK).count().filter(
                    "count > 1")
        if len(duplicate_count.collect()):
            raise ValueError(
                "Duplicated rows found: {}".format(duplicate_count.collect()))
