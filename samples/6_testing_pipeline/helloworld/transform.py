"""
My Custom Transformer
"""

from typing import Dict

import apache_beam.transforms as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.value_provider import ValueProvider
from apache_beam.pvalue import PCollection

from helloworld.base import BaseTransform
from helloworld.dofn import Formatter

__all__ = ["DecorateString"]


class DecorateString(BaseTransform):
    def __init__(self, pipeline_options: PipelineOptions):
        super().__init__(pipeline_options)
        self.formatter = None

    def initiate(self, header: ValueProvider, **options: Dict[str, ValueProvider]):
        super().initiate(**options)
        self.formatter = Formatter(header.get())

    def transform(self, pcoll: PCollection) -> PCollection:
        result = (
            pcoll
            | "Format String" >> beam.ParDo(self.formatter)
            | "Uppercase" >> beam.Map(str.upper)
        )
        return result
