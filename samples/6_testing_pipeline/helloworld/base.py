"""
Base Module For Beam Pipeline Transformation Logic
"""
from abc import ABCMeta, abstractmethod
from typing import Dict

from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.value_provider import ValueProvider
from apache_beam.pvalue import PCollection
from apache_beam.transforms import PTransform


class BaseTransform(PTransform, metaclass=ABCMeta):
    """Abstract base class that defines the overall transformation logic of a Beam Pipeline
    This basically is for a composite transform being configured by static/runtime parameters.

    Methods to be implemented::
    * `__init__`: Setup initial states with constructor parameters.
    * `initiate`: Setup initial states with value providers.
    * `transform`: Define the composite transformation logic between input PCollection and desired output PCollection.
    * If `transform` doesn't use any static/runtime parameters, you can skip implementing `__init__/initiate` respectively.

    Sample Class Definition::

        class DoSomething(BaseTransform):
            def __init__(self, static_state, options):
                super().__init__(options)
                self.static_state = static_state
                self.runtime_state = None

            def initiate(self, state_value_provider: ValueProvider, **kwargs):
                self.runtime_state = state_value_provider.get()

            def transform(self, input_pcollection: PCollection) -> PCollection:
                result = (
                    input_pcollection
                    | "Uppercase" >> beam.Map(str.upper)
                    | ${or_do_something_with_your_states}
                )
                return result

    Sample pipeline using the class::

        _ = (
            pipeline
            | beam.io.Read(...)
            | DoSomething(static_state = 1, pipeline_options)
            | beam.io.Write(...)
        )

    """

    def __init__(self, pipeline_options: PipelineOptions):
        """Initialize internal states with static option values"""
        super().__init__()
        self.initiated = False
        self.pipeline_options = pipeline_options

    @abstractmethod
    def initiate(self, **options: Dict[str, ValueProvider]):
        """
        Construct any internal states or tools for `transform` using ValueProviders.
        This code block will be run only once in a lazy way before the transformation process begins.

        You can customize the method signature by separating each named parameter from options for readability.
        e.g.) def initiate(self, v1: ValueProvider, v2: ValueProvider, **options): ..
        """

    @abstractmethod
    def transform(self, pcoll: PCollection) -> PCollection:
        """
        Define a transformation logic between input and output PCollections
        """

    def expand(self, input_or_inputs: PCollection) -> PCollection:
        """
        Apply the transformation logic to process input data into the desired PCollection
        """
        if not self.initiated:
            self.initiate(**(self.pipeline_options.get_all_options()))
            self.initiated = True

        return self.transform(input_or_inputs)
