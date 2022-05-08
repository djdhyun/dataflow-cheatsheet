import argparse
import logging
import platform
from typing import List

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import WriteToText

class Formatter(beam.DoFn):
    def __init__(self, header):
        self.header = header

    def process(self, row):
        result = '[%s] %s' % (self.header, row)
        yield result

def run(header: str, output: str, beam_args: List[str] = None) -> None:
    pipeline_options = PipelineOptions(beam_args)

    with beam.Pipeline(options=pipeline_options) as pipeline:
        lines = pipeline | "Read Data" >> beam.Create([
           "Hello", "World!", platform.platform()
        ])

        transformed = (
           lines
           | "Format String" >> beam.ParDo(Formatter(header))
           | "Uppercase" >> beam.Map(str.upper)
        )

        output = (
           transformed
           | 'Write' >> WriteToText(output)
        )

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.WARNING)

    parser = argparse.ArgumentParser()
    parser.add_argument("--header", required=True)
    parser.add_argument("--output", required=True)
    args, beam_args = parser.parse_known_args()

    run(header=args.header, output=args.output, beam_args=beam_args)
