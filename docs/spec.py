import yaml
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from config import APP_VERSION
from schemas import Entry

spec = APISpec(
    title="data-contract-ml-pipeline",
    version=APP_VERSION,
    openapi_version="2.0",
    info=dict(description="Data Contract For Machine Learning Pipeline"),
    plugins=[MarshmallowPlugin()],
)

spec.components.schema("Input: EntrySchema", schema=Entry)

if __name__ == "__main__":
    try:
        with open("doc.yml", "w") as f:
            yaml.dump(yaml.load(spec.to_yaml(), Loader=yaml.FullLoader), f)
        print("Swagger generated")
    except Exception as e:
        print('Could not generate swagger: {}'.format(e))