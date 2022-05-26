"""
My beam.DoFn Classes
"""
import apache_beam as beam
import emoji

__all__ = ["Formatter"]

# pylint warns the class to implement `urns.RunnerApiFn.to_runner_api_parameter`
# which is dynamically being patched by beam in runtime.
# pylint: disable=abstract-method
class Formatter(beam.DoFn):
    def __init__(self, header: str):
        super().__init__()

        self.header = header
        self.thumb = None

    def setup(self):
        self.thumb = emoji.emojize(":thumbs_up:")

    def process(self, element):
        result = f"{self.thumb} [{self.header}] {element}"
        yield result
