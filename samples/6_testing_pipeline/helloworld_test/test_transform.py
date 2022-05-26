import unittest

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.value_provider import StaticValueProvider
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to

from helloworld.options import AppOptions
from helloworld.transform import DecorateString


def dummy_pipeline_options(header: str) -> AppOptions:
    options = PipelineOptions().view_as(AppOptions)
    options.header = StaticValueProvider(str, header)
    return options


class DecorateStringTest(unittest.TestCase):
    HEADER = "TEST"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = dummy_pipeline_options(cls.HEADER)
        cls.transformer = DecorateString(options)

    def test_formatter(self):
        words = ["hi", "there", "bob"]
        expected = [
            f"👍 [{self.HEADER}] HI",
            f"👍 [{self.HEADER}] THERE",
            f"👍 [{self.HEADER}] BOB",
        ]

        with TestPipeline() as pipeline:
            output = (
                pipeline
                | "Read Data" >> beam.Create(words)
                | "Decorate String" >> self.transformer
            )

            assert_that(output, equal_to(expected), label="CheckOutput")
