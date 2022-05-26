import unittest

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to

from helloworld.dofn import Formatter


class FormatterTest(unittest.TestCase):
    HEADER = "TEST"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.formatter = Formatter(cls.HEADER)

    def test_formatter(self):
        words = ["hi", "there", "bob"]
        expected = [
            f"👍 [{self.HEADER}] hi",
            f"👍 [{self.HEADER}] there",
            f"👍 [{self.HEADER}] bob",
        ]

        with TestPipeline() as p:
            output = (
                p | beam.Create(words) | "Apply Formatter" >> beam.ParDo(self.formatter)
            )

            assert_that(output, equal_to(expected), label="CheckOutput")
