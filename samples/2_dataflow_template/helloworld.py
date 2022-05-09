import argparse
import logging
import platform
from typing import List, Optional

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import WriteToText

class Formatter(beam.DoFn):
    def __init__(self, header):
        self.header = header

    def process(self, row):
        result = '[%s] %s' % (self.header.get(), row)
        yield result

class AppOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument('--header')
        parser.add_value_provider_argument('--output')


def run(beam_args: List[str] = None) -> None:
   app_options = AppOptions(beam_args)

   with beam.Pipeline(options=app_options) as pipeline:
       lines = pipeline | "Read Data" >> beam.Create([
           "Hello", "World!", platform.platform()
       ])

       transformed = (
           lines
           | "Format String" >> beam.ParDo(Formatter(app_options.header))
           | "Uppercase" >> beam.Map(str.upper)
       )

       output = (
           transformed
           | 'Write' >> WriteToText(app_options.output)
       )

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    args, beam_args = parser.parse_known_args()

    run(beam_args=beam_args)
