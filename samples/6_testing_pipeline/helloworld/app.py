import argparse
import logging
import platform
from typing import List

import apache_beam as beam
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions

from helloworld.options import AppOptions
from helloworld.transform import DecorateString


def run(pipeline_args: List[str] = None) -> None:
    options = PipelineOptions(pipeline_args)
    app_options = options.view_as(AppOptions)

    with beam.Pipeline(options=app_options) as pipeline:
        lines = pipeline | "Read Data" >> beam.Create(
            ["Hello", "World!", platform.platform()]
        )

        transformed = lines | DecorateString(app_options)

        _ = transformed | "Write" >> WriteToText(app_options.output)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    argparser = argparse.ArgumentParser()
    _, args = argparser.parse_known_args()

    run(args)
